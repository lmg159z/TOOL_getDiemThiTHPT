

thong_ke =[]

nameFile ={
    "01": "Hà Nội",
    "02": "TP. Hồ Chí Minh",
    "03": "Hải Phòng",
    "04": "Đà Nẵng",
    "05": "Hà Giang",
    "06": "Cao Bằng",
    "07": "Lai Châu",
    "08": "Lào Cai",
    "09": "Tuyên Quang",
    "10": "Lạng Sơn",
    "11": "Bắc Kạn",
    "12": "Thái Nguyên",
    "13": "Yên Bái",
    "14": "Sơn La",
    "15": "Phú Thọ",
    "16": "Vĩnh Phúc",
    "17": "Quảng Ninh",
    "18": "Bắc Giang",
    "19": "Bắc Ninh",
    "20": "Hà Nam",
    "21": "Nam Định",
    "22": "Thái Bình",
    "23": "Ninh Bình",
    "24": "Thanh Hóa",
    "25": "Nghệ An",
    "26": "Hà Tĩnh",
    "27": "Quảng Bình",
    "28": "Quảng Trị",
    "29": "Thừa Thiên Huế",
    "30": "Đà Nẵng",
    "31": "Quảng Nam",
    "32": "Quảng Ngãi",
    "33": "Bình Định",
    "34": "Phú Yên",
    "35": "Khánh Hòa",
    "36": "Ninh Thuận",
    "37": "Bình Thuận",
    "38": "Kon Tum",
    "39": "Gia Lai",
    "40": "Đắk Lắk",
    "41": "Đắk Nông",
    "42": "Lâm Đồng",
    "43": "Bình Phước",
    "44": "Tây Ninh",
    "45": "Bình Dương",
    "46": "Đồng Nai",
    "47": "Bà Rịa - Vũng Tàu",
    "48": "Long An",
    "49": "Đồng Tháp",
    "50": "An Giang",
    "51": "Tiền Giang",
    "52": "Bến Tre",
    "53": "Trà Vinh",
    "54": "Vĩnh Long",
    "55": "Cần Thơ",
    "56": "Hậu Giang",
    "57": "Kiên Giang",
    "58": "Sóc Trăng",
    "59": "Bạc Liêu",
    "60": "Cà Mau",
    "61": "Điện Biên",
    "62": "Đắk Nông",
    "63": "Hậu Giang",
    "64": "Cục Nhà trường - Bộ Quốc phòng"
}

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

  
  