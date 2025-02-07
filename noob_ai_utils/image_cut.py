from PIL import Image, ImageOps, ImageSequence
from PIL.PngImagePlugin import PngInfo
import folder_paths
import os
import node_helpers
import hashlib
import numpy as np
import torch
import comfy.model_management

TARGET_RESOLUTIONS = [
        (768, 1344), (832, 1216), (896, 1152), (1024, 1024),
        (1152, 896), (1216, 832), (1344, 768)
    ]

class ImageCut2NoobAI:
    

    def __init__(self):
        self.device = comfy.model_management.intermediate_device()
    
    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {"required":
                    {
                        "image": (sorted(files), {"image_upload": True}),
                    }
                    
                }
    
    def image_cut(self, image):
        image_path = folder_paths.get_annotated_filepath(image)

        img = node_helpers.pillow(Image.open, image_path)

        output_images = []
        w, h = None, None

        excluded_formats = ['MPO']

        for i in ImageSequence.Iterator(img):
            i = node_helpers.pillow(ImageOps.exif_transpose, i)

            if i.mode == 'I':
                i = i.point(lambda i: i * (1 / 255))
            image = i.convert("RGB")

            # **添加缩放逻辑**
            target_w, target_h = self.get_proportion(image.size[0],image.size[1])

            new_width = target_w
            aspect_ratio = image.size[1] / image.size[0]  # 计算原始高宽比
            new_height = int(new_width * aspect_ratio)  # 按比例计算新高度
            image = image.resize((new_width, new_height), Image.LANCZOS)  # 高质量缩放

            if new_height > target_h:
                # **高度大于 768，进行对称裁剪**
                crop_y1 = (new_height - target_h) // 2
                crop_y2 = crop_y1 + target_h
                image = image.crop((0, crop_y1, new_width, crop_y2))  # 左上右下坐标
            elif new_height < target_h:
                # **高度小于 768，补黑边**
                padding_top = (target_h - new_height) // 2
                padding_bottom = target_h - new_height - padding_top
                image = ImageOps.expand(image, (0, padding_top, 0, padding_bottom), fill=(0, 0, 0))  # RGB黑色填充


            if len(output_images) == 0:
                w = image.size[0]
                h = image.size[1]

            if image.size[0] != w or image.size[1] != h:
                continue

            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]

            output_images.append(image)

        if len(output_images) > 1 and img.format not in excluded_formats:
            output_image = torch.cat(output_images, dim=0)
        else:
            output_image = output_images[0]

        latent = torch.zeros([1, 4, h // 8, w // 8], device=self.device)
        return (output_image, {"samples":latent})
    
    @classmethod
    def IS_CHANGED(s, image):
        image_path = folder_paths.get_annotated_filepath(image)
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()

    @classmethod
    def VALIDATE_INPUTS(s, image):
        if not folder_paths.exists_annotated_filepath(image):
            return "Invalid image file: {}".format(image)

        return True
    
    @classmethod
    def get_proportion(cls,width: int, height: int):
        result = width / height
        diff = {}
        
        for resolution in TARGET_RESOLUTIONS:
            resolution_ratio = resolution[0] / resolution[1]
            diff[resolution] = abs(result - resolution_ratio)
        
        return min(diff, key=diff.get)


 
    RETURN_TYPES = ("IMAGE", 'LATENT')
    RETURN_NAMES = ("IMAGE", 'LATENT')
 
    FUNCTION = "image_cut"
 
    CATEGORY = "NoobAIUtils/ImageCut2NoobAI"
 

