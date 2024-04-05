import requests
import json
from datetime import datetime

class HttpUtils:
    @staticmethod
    def get_http_content(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        return response.text

class Wallpaper:
    BING_API = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1612409408851&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160"
    BING_URL = "https://cn.bing.com"

    @staticmethod
    def main():
        http_content = HttpUtils.get_http_content(Wallpaper.BING_API)
        data = json.loads(http_content)
        image_info = data["images"][0]

        # 图片地址
        url = Wallpaper.BING_URL + image_info["url"]
        url = url.split('&')[0]

        # 图片时间
        end_date = image_info["enddate"]

        # 图片版权
        copyright = image_info["copyright"]

        # 格式化为 MD 格式
        text = "{0} | [{1}]({2})\n".format(end_date, copyright, url)

        # 写入 MD 文件，使用 UTF-8 编码
        with open("README.md", "w", encoding="utf-8") as file:
            file.write("## Bing Wallpaper\n")
            file.write(text)

if __name__ == "__main__":
    Wallpaper.main()
