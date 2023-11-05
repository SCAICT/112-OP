import requests

url = "https://w3.tcivs.tc.edu.tw/ischool/widget/site_news/news_query_json.php"
data = {"field": "time", "order": "DESC", "pageNum": "0", "maxRows": "25", "keyword": "", "uid": "WID_0_2_a18324d5b18f53971c1d32b13dcfe427c6c77ed4", "tf": "1", "auth_type": "user"}
response = requests.post(url, data=data)
if response.status_code == 200:
    news_data = response.json()

    latest_news = news_data[1:6]
    for news in latest_news:
        date = news['time']
        title = news['title']
        news_id = news['newsId']
        
        print(f"日期: {date}\n{title},\nhttps://w3.tcivs.tc.edu.tw/ischool/public/news_view/show.php?nid={news_id}\n\n")
else:
    print(f"失敗代碼: {response.status_code}")
