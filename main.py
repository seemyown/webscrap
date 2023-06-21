import requests
from fake_headers import Headers
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
url = 'https://habr.com/ru/all/'
headers = Headers("firefox", "win").generate()
output_counter = 0

response = requests.get(url, headers=headers).text
main_html = bs4.BeautifulSoup(response, "lxml")

div_articles_list = main_html.find("div", class_="tm-articles-list")
for articles in div_articles_list.find_all("div", class_="tm-article-snippet tm-article-snippet"):
    time = articles.find("span", class_="tm-article-datetime-published")
    full_time = time.find("time")["title"]
    h2_tag = articles.find("h2", class_="tm-title tm-title_h2")
    link = h2_tag.find("a")["href"]
    title = h2_tag.find("span").text
    post_text = articles.find("p")
    if post_text is not None:
        post_text = post_text.text
    if any(keyword in title for keyword in KEYWORDS):
        if any(keyword in post_text for keyword in KEYWORDS):
            print(title, full_time, url[:16]+link)
            output_counter +=1
        

if output_counter == 0:
    print("Статей по интересу нет")
    
        