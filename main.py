import requests
import json

class HttpUtils:
    @staticmethod
    def get_http_content(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        return response.json()

class Wallpaper:
    BING_API = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1612409408851&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160"
    BING_URL = "https://cn.bing.com"

    @staticmethod
    def main():
        data = HttpUtils.get_http_content(Wallpaper.BING_API)
        image_info = data["images"][0]

        # 提取图片信息
        image_url = Wallpaper.BING_URL + image_info["url"]
        description = image_info["title"]

        # 构造 Markdown 格式的文本，直接将链接替换为图片链接
        text = "## {0} | [{1}]({2})\n![]({3})\n".format(image_info["enddate"], description, image_url, image_url)

        # 读取已存在的内容
        with open("README.md", "r", encoding="utf-8") as file:
            existing_content = file.read()

        # 将新内容插入到旧内容之前
        new_content = text + existing_content

        # 写入 MD 文件，使用 UTF-8 编码
        with open("README.md", "w", encoding="utf-8") as file:
            file.write(new_content)

if __name__ == "__main__":
    Wallpaper.main()


