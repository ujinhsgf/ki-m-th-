import re

def kiem_tra_mat_khau(password):
    path = "0"
    do_dai_hop_le = len(password) >= 8
    if do_dai_hop_le:
        path += " 1"
    co_chu_hoa = any(c.isupper() for c in password)
    if co_chu_hoa:
        path += " 2"
    co_chu_thuong = any(c.islower() for c in password)
    if co_chu_thuong:
        path += " 3"
    co_so = any(c.isdigit() for c in password)
    if co_so:
        path += " 4"
    co_ky_tu_dac_biet = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    if co_ky_tu_dac_biet:
        path += " 5"
    
    if do_dai_hop_le and co_chu_hoa and co_chu_thuong and co_so and co_ky_tu_dac_biet:
        path += " 6"
        return "Hợp lệ", path
    path += " 7"
    return "Không hợp lệ", path

test_cases = [
    ("Abc!1234", "Hợp lệ"),  # B1: Hợp lệ
    ("Ab!12", "Không hợp lệ"),  # B2: Thiếu độ dài
    ("abc!1234", "Không hợp lệ"),  # B3: Thiếu chữ hoa
    ("ABC!1234", "Không hợp lệ"),  # B4: Thiếu chữ thường
    ("Abcdefgh", "Không hợp lệ"),  # B5: Thiếu số
    ("Abc12345", "Không hợp lệ"),  # B6: Thiếu ký tự đặc biệt
    ("1234567", "Không hợp lệ"),  # B7: Tất cả đều sai
    ("Password!", "Không hợp lệ"),  # B8: Thiếu số
    ("Pass123", "Không hợp lệ"),  # B9: Thiếu ký tự đặc biệt và độ dài < 8
    ("!@#$%^&*", "Không hợp lệ"),  # B10: Không có chữ cái hoặc số
    ("StrongPass1!", "Hợp lệ"),  # B11: Hợp lệ
]
for i, (pw, expected) in enumerate(test_cases, 1):
    result = kiem_tra_mat_khau(pw)
    print(f"Test case {i}: {pw} -> {result} ")
