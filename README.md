# Web Scraping Vietnamnet - Dữ liệu Tin Tức

## Mô Tả Dự Án
Dự án này là một chương trình web scraping được xây dựng bằng Python để thu thập các bài viết từ trang web Vietnamnet, đặc biệt là mục "Đời sống" và các mục tin tức khác như Công nghệ, Kinh doanh, Giải trí, Sức khỏe, và Thế giới. Các bài viết sẽ được lưu vào các tệp Excel dưới dạng bảng chứa các thông tin như tiêu đề, mô tả, hình ảnh, và liên kết.

Chương trình sử dụng các thư viện Python như `requests`, `BeautifulSoup`, `pandas`, và `schedule` để thực hiện các công việc sau:
- Lấy dữ liệu từ các bài viết.
- Lưu trữ dữ liệu vào tệp Excel.
- Thực hiện tìm kiếm bài viết.
- Mở trang web trong trình duyệt mặc định.
- Chạy một công việc tự động vào mỗi ngày lúc 22:45 (hoặc thời gian tùy chỉnh).

## Các Thư Viện Cần Cài Đặt
Để chạy dự án này, bạn cần cài đặt các thư viện sau:
```bash
pip install requests beautifulsoup4 pandas schedule
```
## Các Chức Năng Chính
### 1. Mở trang web trong trình duyệt
Chương trình sử dụng hàm open_browser() để tự động mở trang web "https://vietnamnet.vn/doi-song" trong trình duyệt mặc định.
### 2. Web Scraping
Chương trình thực hiện web scraping trên trang "Đời sống" của Vietnamnet và các mục tin tức khác. Sau khi lấy dữ liệu từ các bài viết, chương trình sẽ lưu các thông tin quan trọng vào tệp Excel. Các thông tin bao gồm:
Tiêu đề của bài viết.
Mô tả ngắn của bài viết.
Hình ảnh (URL của ảnh).
Liên kết đến bài viết đầy đủ.
### 3. Tìm kiếm bài viết
Chương trình hỗ trợ tìm kiếm các bài viết trên Vietnamnet theo từ khóa nhập vào. Hàm search_articles(search_query) sẽ gửi yêu cầu tìm kiếm và trả về danh sách các bài viết phù hợp với từ khóa tìm kiếm.
### 4. Công việc tự động hàng ngày
Chương trình được cấu hình để chạy tự động vào mỗi 06:00 hàng ngày thông qua thư viện schedule. Công việc sẽ thực hiện các hành động sau:
Thu thập dữ liệu từ trang chủ.
Thu thập dữ liệu từ các mục tin tức (Công nghệ, Kinh doanh, Giải trí, Sức khỏe, Thế giới).
Lưu dữ liệu vào các tệp Excel tương ứng.
Sau khi hoàn thành, chương trình sẽ tự động dừng lại.
### 5. Các File Excel Được Tạo
Chương trình sẽ lưu kết quả thu thập được từ các bài viết vào các tệp Excel sau:
news_data.xlsx - Dữ liệu từ trang chủ.
category_{tên_mục}.xlsx - Dữ liệu từ các mục tin tức.
## Cách Chạy Chương Trình
Để chạy chương trình, bạn chỉ cần thực hiện lệnh sau trong terminal:
```bash
python scraper.py
```
Chương trình sẽ tự động mở trang web, thu thập dữ liệu và lưu vào các tệp Excel theo lịch trình hàng ngày.
## Tóm tắt các tính năng
Tự động thu thập dữ liệu từ các bài viết tin tức.
Lưu trữ dữ liệu vào tệp Excel.
Mở trang web tự động trong trình duyệt.
Tự động thực hiện công việc vào lúc 06:00 mỗi ngày
Hỗ trợ tìm kiếm bài viết theo từ khóa.