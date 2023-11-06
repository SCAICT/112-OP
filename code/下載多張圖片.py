import requests
image_links = [
    "https://picsum.photos/200/300","https://picsum.photos/200/300",
    "https://picsum.photos/200/300","https://picsum.photos/200/300",
    "https://picsum.photos/200/300",
]
for index, link in enumerate(image_links):
    try:
        response = requests.get(link)
        response.raise_for_status()
        with open(f"image_{index+1}.jpg", "wb") as file:
            file.write(response.content)
        print(f"圖片{index+1}下載成功")
    except requests.exceptions.RequestException as e:
        print(f"圖片{index+1}下載失敗: {e}")