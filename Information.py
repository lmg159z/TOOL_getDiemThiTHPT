

thong_ke =[]

nameFile  = {
  "01": "Sở GD&ĐT Hà Nội",
  "02": "Sở GD&ĐT TP. Hồ Chí Minh",
  "03": "Sở GD&ĐT Hải Phòng",
  "04": "Sở GD&ĐT Đà Nẵng",
  "Q5": "Sở GD&ĐT Hà Giang",
  "06": "Sở GD&ĐT Cao Bằng",
  "07": "Sở GD&ĐT Lai Châu",
  "08": "Sở GD&ĐT Lào Cai",
  "09": "Sở GD&ĐT Tuyên Quang",
  "10": "Sở GD&ĐT Lạng Sơn",
  "11": "Sở GD&ĐT Bắc Kạn",
  "12": "Sở GD&ĐT Thái Nguyên",
  "13": "Sở GD&ĐT Yên Bái",
  "14": "Sở GD&ĐT Sơn La",
  "15": "Sở GD&ĐT Phú Thọ",
  "16": "Sở GD&ĐT Vĩnh Phúc",
  "17": "Sở GD&ĐT Quảng Ninh",
  "18": "Sở GD&ĐT Bắc Giang",
  "19": "Sở GD&ĐT Bắc Ninh",
  "21": "Sở GD&ĐT Hải Dương",
  "22": "Sở GD&ĐT Hưng Yên",
  "23": "Sở GD&ĐT Hoà Bình",
  "24": "Sở GD&ĐT Hà Nam",
  "25": "Sở GD&ĐT Nam Định",
  "26": "Sở GD&ĐT Thái Bình",
  "27": "Sở GD&ĐT Ninh Bình",
  "28": "Sở GD&ĐT Thanh Hóa",
  "29": "Sở GD&ĐT Nghệ An",
  "30": "Sở GD&ĐT Hà Tĩnh",
  "31": "Sở GD&ĐT Quảng Bình",
  "32": "Sở GD&ĐT Quảng Trị",
  "33": "Sở GD&ĐT Thừa Thiên-Huế",
  "34": "Sở GD&ĐT Quảng Nam",
  "35": "Sở GD&ĐT Quảng Ngãi",
  "36": "Sở GD&ĐT Kon Tum",
  "37": "Sở GD&ĐT Bình Định",
  "38": "Sở GD&ĐT Gia Lai",
  "39": "Sở GD&ĐT Phú Yên",
  "40": "Sở GD&ĐT Đắk Lắk",
  "41": "Sở GD&ĐT Khánh Hòa",
  "42": "Sở GD&ĐT Lâm Đồng",
  "43": "Sở GD&ĐT Bình Phước",
  "44": "Sở GD&ĐT Bình Dương",
  "45": "Sở GD&ĐT Ninh Thuận",
  "46": "Sở GD&ĐT Tây Ninh",
  "47": "Sở GD&ĐT Bình Thuận",
  "48": "Sở GD&ĐT Đồng Nai",
  "49": "Sở GD&ĐT Long An",
  "50": "Sở GD&ĐT Đồng Tháp",
  "51": "Sở GD&ĐT An Giang",
  "52": "Sở GD&ĐT Bà Rịa-Vũng Tàu",
  "53": "Sở GD&ĐT Tiền Giang",
  "54": "Sở GD&ĐT Kiên Giang",
  "55": "Sở GD&ĐT Cần Thơ",
  "56": "Sở GD&ĐT Bến Tre",
  "57": "Sở GD&ĐT Vĩnh Long",
  "58": "Sở GD&ĐT Trà Vinh",
  "59": "Sở GD&ĐT Sóc Trăng",
  "60": "Sở GD&ĐT Bạc Liêu",
  "61": "Sở GD&ĐT Cà Mau",
  "62": "Sở GD&ĐT Điện Biên",
  "63": "Sở GD&ĐT Đắk Nông",
  "64": "Sở GD&ĐT Hậu Giang",
  "65": "Cục Nhà trường - Bộ Quốc phòng"
};



def convert_format():
    global nameFile
    result = []
    temp = []
    for idx, (key, value) in enumerate(nameFile.items()):
        temp.extend([key, value])
        if (idx + 1) % 2 == 0:
            result.append(temp)
            temp = []
    if temp:
        result.append(temp)  # Thêm phần tử lẻ cuối cùng nếu có
    return result
    
    
def render(value, headers):
  table = tabulate(value, headers=headers, tablefmt="grid")
  print(table)

  
  