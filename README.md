

```
+---------------------------+
| Lê Minh Ghi                                      |
| github.com/lmg159z                               |
+---------------------------+```

```markdown
# Lấy điểm thi tốt nghiệp THPT từ Vietnamnet

## Giới thiệu

Đây là một script Python để tự động lấy điểm thi tốt nghiệp THPT từ website Vietnamnet.vn. Script này cho phép người dùng nhập năm thi, mã hội đồng thi và lấy điểm của các thí sinh theo mã hội đồng hoặc theo khoảng mã hội đồng.

## Yêu cầu

- Python 3.x

## Cài đặt

1. **Cài đặt các thư viện:**
   ```bash
   pip install requests bs4 tabulate unidecode
   ```

## Cách sử dụng

1. **Tạo file `Information.py`:**
   - File `Information.py` chứa các thông tin về mã hội đồng và tên hội đồng thi. Ví dụ:
     ```python
     nameFile = {
         "01": "Sở GD&ĐT TP.Hồ Chí Minh",
         "02": "Sở GD&ĐT Hà Nội",
         "03": "Sở GD&ĐT Hải Phòng",
         # ...
     }
     ```

2. **Chạy script:**
   ```bash
   python index.py
   ```
   - Làm theo hướng dẫn trên màn hình để nhập năm thi, mã hội đồng thi và các tùy chọn khác.

## Cách hoạt động

- Script sử dụng thư viện `requests` để tải dữ liệu từ website Vietnamnet.vn.
- Thư viện `bs4` được sử dụng để phân tích HTML và trích xuất dữ liệu.
- Script sử dụng hàm `extract_data_from_html()` để trích xuất điểm thi từ HTML.
- Dữ liệu được lưu vào file CSV trong thư mục `diem_cac_so`.

## Ví dụ

- **Lấy điểm thi của tất cả thí sinh thuộc hội đồng thi số 01 năm 2023:**
   ```bash
   python index.py
   ```
   - Nhập năm thi: `2023`
   - Nhập mã hội đồng thi: `01`

- **Lấy điểm thi của tất cả thí sinh thuộc hội đồng thi từ số 01 đến số 09 năm 2023:**
   ```bash
   python index.py
   ```
   - Nhập năm thi: `2023`
   - Nhập mã hội đồng thi: `0`
   - Chọn `y` để lấy theo khoảng
   - Nhập mã bắt đầu: `01`
   - Nhập mã kết thúc: `09`

## Lưu ý

- Script này được viết để lấy điểm thi tốt nghiệp THPT từ website Vietnamnet.vn. Nếu website thay đổi cấu trúc, script có thể không hoạt động.
- Script có thể gặp lỗi nếu website bị lỗi hoặc quá tải.

## File đính kèm

- `index.py` - Script Python.
- `Information.py` - File chứa thông tin về mã hội đồng và tên hội đồng thi (ví dụ).

## Liên hệ

Nếu bạn có bất kỳ câu hỏi nào, vui lòng liên hệ với tôi.
```

**Lưu ý:**
- Bạn cần thay thế `Information.py` bằng tên file thực tế của bạn.
- Bạn có thể cần thay đổi một số phần code trong `index.py` để phù hợp với cấu trúc website mới của Vietnamnet.vn.

