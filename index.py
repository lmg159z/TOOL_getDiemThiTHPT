import requests
import os
import Information
from bs4 import BeautifulSoup
from tabulate import tabulate
from unidecode import unidecode
import socket
import time

# Xử lý html sang array
def extract_data_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    table_rows = soup.find_all('tr')
    result_obj = {
        "Toán": "-",
        "Văn": "-",
        "Sử": "-",
        "Địa": "-",
        "Ngoại ngữ": "-",
        "GDCD": "-",
        "Lí": "-",
        "Hóa": "-",
        "Sinh": "-"
    }
    for row in table_rows:
        columns = row.find_all('td')
        if len(columns) == 2:
            subject = columns[0].text.strip()
            value = columns[1].text.strip()
            result_obj[subject] = value
    return ", ".join(list(result_obj.values()))

url = "https://vietnamnet.vn/giao-duc/diem-thi/tra-cuu-diem-thi-tot-nghiep-thpt"

# Hàm kiểm tra kết nối internet
def check_internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        return False

# Lấy HTML
check = 0
tong = 0
def get_html(mhd, year, start):
    global check, tong
    try:
        response = requests.get(url + "/" + year + "/" + mhd + start + ".html")
        if response.status_code == 200:
            html_content = response.text
            start_marker = "<div class=\"resultSearch__right\">"
            end_marker = "<div class=\"lg:hidden flex justify-center\"> <!-- BEGIN COMPONENT:: COMPONENT000055 -->"
            extracted_data = html_content.split(start_marker)[1].split(end_marker)[0]
            listVakue = extract_data_from_html(extracted_data)
            # print(extracted_data)
            return [True, listVakue, [mhd + start, Information.nameFile[mhd]]]
            check = 0
            tong += 1
        else:
            check += 1
            print("\033[1;31m Không thể lấy dữ liệu từ trang web.")
            return [False, "", []]
    except requests.exceptions.RequestException as e:
        print("\033[1;31m Không thể kết nối tới trang web.")
        return [False, "", []]

# Ghi vào file
def write_to_file(data, nameFile):
    os.makedirs("diem_cac_so", exist_ok=True)
    with open(nameFile + ".csv", "a") as f:
        f.write(data + "\n")

def convert_to_filename(text):
    no_diacritics = unidecode(text)
    filename = no_diacritics.replace(" ", "_")
    return filename

def render(value, headers):
    table = tabulate(value, headers=headers, tablefmt="grid", colalign=("left", "right"))
    print(table)

def renderInfo():
    os.system("clear")
    print("\033[1;33m")
    render(Information.convert_format(), ["Mã Hội Đồng", "Tên Hội Đồng Thi", "Mã Hội Đồng", "Tên Hội Đồng Thi"])
    print("\033[0m")

# Chạy chương trình
def run(start, mhdStart, year):
    global check, tong
    start = start
    while check <= 10:
        if not check_internet():
            print("Không có kết nối internet. Đang chờ kết nối lại...")
            while not check_internet():
                time.sleep(5)

        tong += 1
        print(tong)
        go = f"{start:06d}"
        value = get_html(mhdStart, year, go)
        
        if value[0]:
            os.system("clear")
            luuTam = value[2] + value[1].split(",")
            render([
                [" \033[1;34m Số Báo Danh", luuTam[0]],
                ["Sở Giáo Dục Đào Tạo", luuTam[1]],
                ["Toán", luuTam[2]],
                ["Ngữ Văn", luuTam[3]],
                ["Lịch Sử", luuTam[4]],
                ["Địa Lí", luuTam[5]],
                ["Ngoại Ngữ", luuTam[6]],
                ["Giáo Dục Công Dân", luuTam[7]],
                ["Vật Lý", luuTam[8]],
                ["Hoá Học", luuTam[9]],
                ["Sinh Học", luuTam[10]]
            ], "")
            
            nameFile = convert_to_filename(Information.nameFile[mhdStart])
            write_to_file(luuTam[1] +", " +mhdStart + go + ", " + value[1], "./diem_cac_so/" + nameFile)
            check = 0
        start += 1
    Information.thong_ke.append([Information.nameFile[str(mhdStart)], tong - 11])
    tong = 0
    check = 0

renderInfo()
year = input("\033[1;36m Vui long nhap nam muon lay ==> ")
renderInfo()
mhd = input("\033[1;36m Vui long nhap ma hoi dong thi \nNhap 0 de lay tay ca \n ==> ")
renderInfo()
if int(mhd) > 0 and int(mhd) <= 65:
    run(1, mhd, year)
else:
    renderInfo()
    checkGet = input("\033[1;36m Nhap y de lay theo khoang ( 01 - 09) \nNhap n de lay het tat ca \n ==> ")
    renderInfo()
    if checkGet == "y":
        mStart = int(input("\033[1;36m Nhap ma bat dau: => "))
        mEnd = int(input("\033[1;36m Nhap ma ket thuc: => "))
        if mStart < mEnd and mStart > 0 and mEnd <= 65:
            while mStart <= mEnd:
                if len(str(mStart)) == 1:
                    ma = "0" + str(mStart)
                run(1, ma, year)
                mStart += 1
    else:
        Start = 1
        while Start <= 65:
            if len(str(Start)) == 1:
                ma = "0" + str(Start)
            run(1, ma, year)
            Start += 1

render(Information.thong_ke, ["\033[7m Sở GDDT", "Số Lượng Sỉ Tủ"])