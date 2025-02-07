import os
import folder_paths
import hashlib
import node_helpers
from PIL import Image,ImageSequence,ImageOps
import numpy as np
import torch

class GetArtistStyle:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        # input_dir = folder_paths.get_input_directory()
        input_dir = folder_paths.get_folder_paths("custom_nodes")[0]
        input_dir = os.path.join(input_dir, "sanjin-noobAI-utils/noob_ai_utils/artist")
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {"required":
                    {
                        "image": (sorted(files), {
                            "image_upload": True
                        }),
                        "strength": ("FLOAT", {"default": 1, "min": 0.1, "max": 2, "step": 0.1,"round": 0.1})
                     },
                    
                }

    def create_prompt(self, image, strength):
        artist_name = image.split('.')[0]

        print("artist_name",artist_name)
        print("strength",strength)

        if strength != 1:
            result = f"({artist_name} : {strength}),"
        else:
            result = f"{artist_name},"

        return (result,)




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
    
    OUTPUT_NODE = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
 
    FUNCTION = "create_prompt"
 
    CATEGORY = "NoobAIUtils/GetArtistStyle"
 