import requests,os, Information
from bs4 import BeautifulSoup
from tabulate import tabulate
from unidecode import unidecode
#//// xử lý html sang array
def extract_data_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    table_rows = soup.find_all('tr')
    # Khởi tạo đối tượng (dictionary) để lưu giá trị
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
    # Lấy giá trị từ mỗi dòng <tr>
    for row in table_rows:
        columns = row.find_all('td')
        if len(columns) == 2:
            subject = columns[0].text.strip()
            value = columns[1].text.strip()
            result_obj[subject] = value
    #diem_list = list(result.values())
    #print (result_obj)
    return ", ".join(list(result_obj.values()))
 
url = "https://vietnamnet.vn/giao-duc/diem-thi/tra-cuu-diem-thi-tot-nghiep-thpt"

#/////get_html/////////
check = 0
tong = 0
def get_html(mhd,year,start):
  global check, tong
  response = requests.get(url+"/"+year+"/"+mhd+start+".html")
  if response.status_code == 200:
      html_content = response.text
      start_marker = "<div class=\"resultSearch__right\">"
      end_marker = "<div class=\"lg:hidden flex justify-center\"> <!-- BEGIN COMPONENT:: COMPONENT000055 -->"
      extracted_data = html_content.split(start_marker)[1].split(end_marker)[0]
     # print(extracted_data)
      #return extracted_data
      listVakue = extract_data_from_html(extracted_data)
      return [True,listVakue ,[ mhd+start,Information.nameFile[mhd]]]
      check = 0
      tong +=1 
  else:
      check +=1
      print("\033[1;31m Không thể lấy dữ liệu từ trang web.")
      return [False, "",[]]


#/////write to files////
def write_to_file(data,nameFile):
  os.makedirs("diem_cac_so", exist_ok=True)
  with open(nameFile+".csv", "a") as f:
    f.write(data + "\n")
    
def convert_to_filename(text):
    # Loại bỏ các ký tự có dấu
    no_diacritics = unidecode(text)
    # Thay thế khoảng trắng bằng gạch dưới
    filename = no_diacritics.replace(" ", "_")
    return filename

def render(value, headers):
  table = tabulate(value, headers=headers, tablefmt="grid", colalign=("left", "right"))
  print(table)
  
def renderInfo():
  os.system("clear")
  print("\033[1;33m")
  render(Information.convert_format(),["Mã Hội Đồng", "Tên Hội Đồng Thi","Mã Hội Đồng", "Tên Hội Đồng Thi"])
  print("\033[0m")
  
  
  
#////start/////
def run(start, mhdStart, year):
  global check, tong
  start = start
  while check <= 10:
    tong+=1
    print(tong) 
    if len(str(start)) == 1:
      go = "00000" + str(start) 
    if len(str(start)) == 2:
      go = "0000" + str(start) 
    if len(str(start)) == 3:
      go = "000" + str(start)  
    if len(str(start)) == 4:
      go = "00" + str(start)  
    if len(str(start)) == 5:
      go = "0" + str(start) 
    if len(str(start)) == 6:
      go = str(start) 
    value = get_html(mhdStart,year, go) 
    
    if value[0]:
      #print(mhdStart+go+": "+value[1])
      #print(value[2]+value[1].split(","))
      os.system("clear")
      #render([value[2]+value[1].split(",")],["Số Báo Danh","Sở GDĐT","Toán","Văn","L.Sử","Địa.L","N.Ngữ","GDCD","V.Lí","Hoá.H","Sinh.H"])
      luuTam = value[2]+value[1].split(",")
      render([
        [" \033[1;34m Số Báo Danh",luuTam[0]],
        ["Sở Giáo Dục Đào Tạo",luuTam[1]],
        ["Toán",luuTam[2]],
        ["Ngữ Văn",luuTam[3]],
        ["Lịch Sử",luuTam[4]],
        ["Địa Lí",luuTam[5]],
        ["Ngoại Ngữ",luuTam[6]],
        ["Giáo Dục Công Dân",luuTam[7]],
        ["Vật Lý",luuTam[8]],
        ["Hoá Học",luuTam[9]],
        ["Sinh Học",luuTam[10]]
        ],""
        )
      
      nameFile = convert_to_filename(Information.nameFile[mhdStart])
      write_to_file(mhdStart+go+", "+value[1],"./diem_cac_so/" + nameFile)
      write_to_file(mhdStart+go+", "+value[1], "diem_so_tong")
      start +=1
      #--------
  Information.thong_ke.append([Information.nameFile[str(mhdStart)],tong - 11])   
  tong = 0
  check = 0
  

renderInfo()
year = input("\033[1;36m Vui long nhap nam muon lay ==> ")
renderInfo()
mhd = input("\033[1;36m Vui long nhap ma hoi dong thi \nNhap 0 de lay tay ca \n ==> ")
renderInfo()
if int(mhd) > 0 and int(mhd) < 65:
  run(1, mhd, year)
else:
  renderInfo()
  checkGet = input("\033[1;36m Nhap y de lay theo khoang ( 01 - 09)  \nNhap n de lay het tat ca \n ==> ")
  renderInfo()
  if checkGet == "y":
    mStart = int(input("\033[1;36m Nhap ma bat dau: => "))
    mEnd = int(input("\033[1;36m Nhap ma ket thuc: => "))
    if mStart < mEnd and mStart > 0 and mEnd <= 64:
      while mStart <= mEnd:
        if len(str(mStart)) == 1:
          ma = "0" + str(mStart)
        run(1, ma, year)
        mStart +=1 
  else:
   Start = 1
   while Start <= 64:
    if len(str(Start)) == 1:
       ma = "0" + str(Start)
    run(1, ma, year)
    Start +=1 
 # get_html("01","2023","000955")
 # print(extract_data_from_html(get_html()))
 
 
render(Information.thong_ke,["\033[7m Sở GDDT","Số Lượng Sỉ Tủ"])