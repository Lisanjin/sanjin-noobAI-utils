from .noob_ai_utils.image_cut import ImageCut2NoobAI
from .noob_ai_utils.artist_prompt import GetArtistStyle

NODE_CLASS_MAPPINGS = {
    "image_cut": ImageCut2NoobAI,
    "artist_prompt": GetArtistStyle
}
 
NODE_DISPLAY_NAME_MAPPINGS = {
    "image_cut": "图片切割至noobai推荐大小",
    "artist_prompt": "画师风格快速获取"
}

all = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']