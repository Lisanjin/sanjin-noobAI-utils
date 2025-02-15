from .noob_ai_utils.image_cut import ImageCut2NoobAI
from .noob_ai_utils.artist_prompt import GetArtistStyle
from .noob_ai_utils.create_empty_latent import CreateEmptyLatent
from .noob_ai_utils.danbooru_tag import Image2DanbooruTag

NODE_CLASS_MAPPINGS = {
    "image_cut": ImageCut2NoobAI,
    "artist_prompt": GetArtistStyle,
    "create_empty_latent": CreateEmptyLatent,
    "danbooru_tag":Image2DanbooruTag
}
 
NODE_DISPLAY_NAME_MAPPINGS = {
    "image_cut": "图片切割至noobai推荐大小",
    "artist_prompt": "画师风格快速获取",
    "create_empty_latent": "快速创建noobaiXL空latent",
    "danbooru_tag":"获取Danbooru tag"
}

all = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']