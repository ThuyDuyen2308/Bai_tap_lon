import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
import sys
import webbrowser

def open_browser():
    url = 'https://vietnamnet.vn/doi-song'
    webbrowser.open(url)
    print(f"Đang mở trang web: {url}")

def scrape_news():
    url = 'https://vietnamnet.vn/doi-song'
    print(f"Đang gửi yêu cầu đến {url}...")

    response = requests.get(url)
    print(f"Mã trạng thái HTTP: {response.status_code}")

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        articles = soup.find_all('div', class_='horizontalPost')
        print(f"Đã tìm thấy {len(articles)} bài viết")

        data = []

        for article in articles:

            title_tag = article.find('h3', class_='horizontalPost__main-title')
            title = title_tag.get_text(strip=True) if title_tag else 'No title'

            description_tag = article.find('div', class_='horizontalPost__main-desc')
            description = description_tag.get_text(strip=True) if description_tag else 'No description'

            image_tag = article.find('img')
            image_url = image_tag['src'] if image_tag else 'No image'

            link_tag = article.find('a', href=True)
            link = 'https://vietnamnet.vn' + link_tag['href'] if link_tag else 'No link'

            data.append([title, description, image_url, link])

        df = pd.DataFrame(data, columns=['Tiêu đề', 'Mô tả', 'Hình ảnh', 'Liên kết'])
        df.to_excel('news_data.xlsx', index=False)

        print('Dữ liệu đã được lưu vào file news_data.xlsx')
    else:
        print(f'Không truy cập được trang web: {response.status_code}')

def scrape_category(category_url):
    response = requests.get(category_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', class_='horizontalPost')
        
        category_data = []
        for article in articles:
            title_tag = article.find('h3', class_='horizontalPost__main-title')
            title = title_tag.get_text(strip=True) if title_tag else 'No title'
            description_tag = article.find('div', class_='horizontalPost__main-desc')
            description = description_tag.get_text(strip=True) if description_tag else 'No description'
            image_tag = article.find('img')
            image_url = image_tag['src'] if image_tag else 'No image'
            link_tag = article.find('a', href=True)
            link = 'https://vietnamnet.vn' + link_tag['href'] if link_tag else 'No link'
            category_data.append([title, description, image_url, link])
        
        return category_data
    else:
        print(f"Không truy cập được mục tin tức {category_url}, mã lỗi: {response.status_code}")
        return []

def search_articles(search_query):
    search_url = 'https://vietnamnet.vn/tim-kiem'
    payload = {'q': search_query}

    response = requests.post(search_url, data=payload)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', class_='horizontalPost')
        
        search_data = []
        for article in articles:
            title_tag = article.find('h3', class_='horizontalPost__main-title')
            title = title_tag.get_text(strip=True) if title_tag else 'No title'
            description_tag = article.find('div', class_='horizontalPost__main-desc')
            description = description_tag.get_text(strip=True) if description_tag else 'No description'
            image_tag = article.find('img')
            image_url = image_tag['src'] if image_tag else 'No image'
            link_tag = article.find('a', href=True)
            link = 'https://vietnamnet.vn' + link_tag['href'] if link_tag else 'No link'
            search_data.append([title, description, image_url, link])
        
        return search_data
    else:
        print(f"Không thể thực hiện tìm kiếm: {response.status_code}")
        return []

def job():
    print("Đang lấy dữ liệu.")
    scrape_news()

    categories = [
        'https://vietnamnet.vn/cong-nghe',
        'https://vietnamnet.vn/kinh-doanh',
        'https://vietnamnet.vn/giai-tri',
        'https://vietnamnet.vn/suc-khoe',
        'https://vietnamnet.vn/the-gioi'
    ]
    
    for category_url in categories:
        print(f"Đang lấy dữ liệu từ mục: {category_url}")
        category_data = scrape_category(category_url)
        if category_data:
            df_category = pd.DataFrame(category_data, columns=['Tiêu đề', 'Mô tả', 'Hình ảnh', 'Liên kết'])
            df_category.to_excel(f'category_{category_url.split("/")[-1]}.xlsx', index=False)

    print("Đã hoàn thành công việc, dừng chương trình.")
    sys.exit()

def run_scheduled_task():
    open_browser()
    schedule.every().day.at("06:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
        if not schedule.get_jobs():
            print("Chương trình đã hoàn thành")
            sys.exit()
run_scheduled_task()
