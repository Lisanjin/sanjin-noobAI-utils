import requests
import folder_paths
import os
from bs4 import BeautifulSoup

class Image2DanbooruTag:
    def __init__(self):
        pass

    OUTPUT_NODE = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
 
    FUNCTION = "get_tag"
 
    CATEGORY = "NoobAIUtils/Image2DanbooruTag"

    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {"required":
                    {
                        "image": (sorted(files), {"image_upload": True}),
                    }
                }
    
    def get_tag(self, image):
        url = "http://dev.kanotype.net:8003/deepdanbooru/upload"

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh-HK;q=0.9,zh;q=0.8,en;q=0.7,ja;q=0.6",
            "Cache-Control": "no-cache",
            "Cookie": "_ga=GA1.1.1448537993.1739067999; _ga_KX6PXS8XCN=GS1.1.1739067999.1.1.1739070268.0.0.0",
            "DNT": "1",
            "Origin": "http://dev.kanotype.net:8003",
            "Pragma": "no-cache",
            "Referer": "http://dev.kanotype.net:8003/deepdanbooru/",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        }

        # 打开文件
        print
        with open(image, "rb") as file:
            files = {"file": file}
            data = {
                "network_type": "general",  
                "crop": "false"  
            }

            # 发送POST请求
            session = requests.Session()

            response = session.post(url, files=files, data=data, headers=headers, verify=False)

        if response.status_code == 200:
            print("上传成功")
            soup = BeautifulSoup(response.text, "html.parser")
            td_elements = soup.find_all('td')
            tags = [td.find('a').text for td in td_elements if td.find('a')]
            filtered_tags = [tag for tag in tags if 'rating' not in tag]

            return (",".join(tags),)
        else:
            raise ValueError("fetch error")