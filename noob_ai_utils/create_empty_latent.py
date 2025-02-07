import torch
import comfy.model_management

class CreateEmptyLatent:

    def __init__(self):
        self.device = comfy.model_management.intermediate_device()

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required":{
                "分辨率": (["768x1344", "832x1216", "896x1152", "1024x1024", "1152x896", "1216x832", "1344x768"],),
            }
        }


    def create_empty_latent(self,分辨率):
        w = int(分辨率.split("x")[0])
        h = int(分辨率.split("x")[1])
        latent = torch.zeros([1, 4, h // 8, w // 8], device=self.device)
        return ({"samples":latent},)

    OUTPUT_NODE = True
    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("LATENT",)
    FUNCTION = "create_empty_latent"
    CATEGORY = "NoobAIUtils/CreateEmptyLatent"