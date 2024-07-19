import requests,os, Information
from bs4 import BeautifulSoup
from tabulate import tabulate
from unidecode import unidecode


def render(value, headers):
  os.system("clear")
  table = tabulate(value, headers=headers, tablefmt="grid", colalign=("left", "right"))
  print(table)
  
def renderInfo():
  os.system("clear")
  print("\033[1;33m")
  render(Information.dict_to_list(),["Mã Hội Đồng", "Tên Hội Đồng Thi"])
  print("\033[0m")
  



check = 0
def extract_td_values(url):
    try:
        global check
        # Gửi yêu cầu GET đến trang web
        response = requests.get(url)

        # Kiểm tra nếu yêu cầu thành công
        if response.status_code == 200:
            # Lấy nội dung HTML của trang web
            html_content = response.text

            # Sử dụng BeautifulSoup để phân tích cú pháp HTML
            soup = BeautifulSoup(html_content, 'html.parser')

            # Tìm phần tử <tbody> trong mã HTML
            tbody = soup.find('tbody')

            # Kiểm tra xem có tồn tại <tbody> không
            if tbody:
                # Lấy tất cả các phần tử <td> trong <tbody>
                td_elements = tbody.find_all('td')

                # Kiểm tra xem có ít nhất một phần tử <td> có giá trị không
                if any(td.text.strip() for td in td_elements):
                    # Tạo mảng để lưu trữ giá trị từ các thẻ <td>
                    values = []

                    # Lặp qua từng phần tử <td>
                    for td in td_elements:
                        # Lấy nội dung trong thẻ <td>, nếu không có thì thêm '-'
                        value = td.text.strip() if td.text.strip() else '-'
                        values.append(value)
                    check = 0
                    return values
                else:
                    #print("Không có giá trị trong các thẻ <td> của <tbody>.")
                    check += 1
                    return None

            else:
                print("Không tìm thấy phần tử <tbody> trên trang web.")
                check += 1
                return None

        else:
            print(f"Lỗi khi tải trang web. Mã trạng thái: {response.status_code}")
            check +=1
            return None

    except Exception as e:
        print(f"Lỗi: {str(e)}")
        check +=1
        return None

def run(MaHoiDong):
  global check
  so_luong = 0
  stt = 1
  while check < 10:
    if len(str(stt)) == 1:
      go = "000" + str(stt) 
    if len(str(stt)) == 2:
      go = "00" + str(stt) 
    if len(str(stt)) == 3:
      go = "0" + str(stt) 
    if len(str(stt)) == 4:
      go = str(stt)
      
      #---------
    url = Information.url + MaHoiDong + go
    result = extract_td_values(url)
    if result:
      so_luong +=  1
      result.insert(0,MaHoiDong)
      result.insert(1,Information.nameSchools[MaHoiDong])
      #print(result)
      print("\033[1;32m")
      render( [
          [" Mã Hội Đồng", result[0]],
          ["Tên Hội Đồng", result[1]],
          ["Số Báo Danh", result[2]],
          ["Họ Và Tên", result[3]],
          ["Ngày Sinh", result[4]],
          ["Nơi Sinh", result[5]],
          ["Tên Trường", result[6]],
          ["Điểm Ưu Tiên", result[7]],
          ["Ngữ Văn", result[8]],
          ["Tiếng Anh", result[9]],
          ["Toán", result[10]],
          ["Điểm Chuyên", result[11]] 
          ],"")
      print(" \033[0m")
      nameFile = convert_to_filename(Information.nameSchools[MaHoiDong])
      writeToFile(nameFile, ", ".join(result))
   #############        
    stt +=1  
  if MaHoiDong in Information.nameSchools:
     Information.thong_ke.append([Information.nameSchools[MaHoiDong],so_luong])
  check = 0
  
  
      
#run("0101")


def writeToFile(nameFile,data):
  os.makedirs("diem_don_vi", exist_ok=True)
  with open("./diem_don_vi/" + nameFile+".csv", "a") as f:
    f.write(data + "\n")
  with open("Toan_Bo_Diem.csv", "a") as f:
    f.write(data + "\n")

def convert_to_filename(text):
    # Loại bỏ các ký tự có dấu
    no_diacritics = unidecode(text)
    # Thay thế khoảng trắng bằng gạch dưới
    filename = no_diacritics.replace(" ", "_")
    return filename
    
# Giả sử Information.nameSchools là dictionary chứa các đơn vị và mã của chúng
renderInfo()
option = input("Nhập 'y' để lấy từng đơn vị hoặc 'n' để lấy hết: ")

if option.lower() == 'y':
    renderInfo()
    ma_don_vi = input("Nhập mã đơn vị: ")
    if ma_don_vi in Information.nameSchools:
        print("Bắt đầu chạy...")
        run(ma_don_vi)
    else:
        print("Mã đơn vị không hợp lệ. Kết thúc chương trình.")
elif option.lower() == 'n':
    option_n = input("Nhập 'y' để lấy theo khoảng hoặc 'n' để lấy toàn bộ: ")
    if option_n.lower() == 'y':
        renderInfo()
        ma_bat_dau = input("Nhập mã bắt đầu: ")
        ma_ket_thuc = input("Nhập mã kết thúc: ")
        if ma_bat_dau in Information.nameSchools and ma_ket_thuc in Information.nameSchools and ma_ket_thuc > ma_bat_dau:
            start = ma_bat_dau 
            while start <= ma_ket_thuc:
              run(start)
              start = "{:04d}".format(int(start) + 1)
              
        else:
            print("Mã bắt đầu hoặc mã kết thúc không hợp lệ. Kết thúc chương trình.")
    elif option_n.lower() == 'n':
        print("Bắt đầu chạy...")
        start = "0101"
        while start <= "3000":
          run(start)
          start = "{:04d}".format(int(start) + 1)
 
    else:
        print("Lựa chọn không hợp lệ. Kết thúc chương trình.")
else:
    print("Lựa chọn không hợp lệ. Kết thúc chương trình.")


os.system("clear")
print("Sau đây là bản thống kê:")


with open("Thong_ke.csv", "a") as f:
  for value in Information.thong_ke:
    d = value[0] +", " + str(value[1])
    f.write(d + "\n")




render(
  Information.thong_ke,
  ["Tên Đơn Vị","Số Lượng Thí Sinh"] )
  
  