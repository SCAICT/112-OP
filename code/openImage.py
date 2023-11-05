import requests
from PIL import Image

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/1920px-Cat_August_2010-4.jpg"  # 替換為要下載的圖片連結
response = requests.get(url)

# 檢查圖片是否下載成功
if response.status_code == 200:
    with open("圖片檔名.jpg", "wb") as file:
        file.write(response.content)
        print("圖片下載成功")

    # 打開圖片
    img = Image.open("圖片檔名.jpg")
    img.show()
else:
    print("無法下載圖片")