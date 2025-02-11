# 用于NoobAiXL的一点小工具

## ImageCut2NoobAI

将图片放缩裁剪至NoobAiXL推荐推荐的尺寸，并输出一个同尺寸的latent

## GetArtistStyle

快速生成艺术家风格提示词，需要把例图按Danbooru命名规范重命名后，放入comfyUI/custom_nodes/sanjin-noobAI-utils/noob_ai_utils/artist文件夹

## CreateEmptyLatent

快速生成NoobAiXL推荐推荐的尺寸的空latent

## Image2DanbooruTag

使用deepdanbooru项目，对图片进行提示词反推，以获取适用于Danbooru的tag  
没有使用本地模型，而是使用的在线请求[Deep Danbooru](http://dev.kanotype.net:8003/deepdanbooru/)，因此无法离线使用
