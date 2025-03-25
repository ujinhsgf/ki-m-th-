import re

def kiem_tra_tai_khoan(username, password):
    path = "0"

    #username
    do_dai_username = len(username) >= 5
    if do_dai_username:
        path += " 1"
    khong_ky_tu_dac_biet = bool(re.match(r"^[A-Za-z0-9]+$", username))  # Chỉ chứa chữ và số
    if khong_ky_tu_dac_biet:
        path += " 2"
    khong_trung_mat_khau = username != password
    if khong_trung_mat_khau:
        path += " 3"

    #mật khẩu
    do_dai_hop_le = len(password) >= 8
    if do_dai_hop_le:
        path += " 4"
    co_chu_hoa = any(c.isupper() for c in password)
    if co_chu_hoa:
        path += " 5"
    co_chu_thuong = any(c.islower() for c in password)
    if co_chu_thuong:
        path += " 6"
    co_so = any(c.isdigit() for c in password)
    if co_so:
        path += " 7"
    co_ky_tu_dac_biet = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    if co_ky_tu_dac_biet:
        path += " 8"

    if not do_dai_username or not khong_ky_tu_dac_biet or not khong_trung_mat_khau:
        path += " 9"
        return "Username không hợp lệ", path
    
    if not (do_dai_hop_le and co_chu_hoa and co_chu_thuong and co_so and co_ky_tu_dac_biet):
        path += " 10"
        return "Mật khẩu không hợp lệ", path

    path += " 11"
    return "Tài khoản hợp lệ", path

#test case
test_cases = [
    ("user1", "Abc!1234"),  # Hợp lệ
    ("usr", "Abc!1234"),  # Username quá ngắn
    ("user1", "abc12345"),  # Mật khẩu thiếu ký tự đặc biệt
    ("user1", "ABC!1234"),  # Mật khẩu thiếu chữ thường
    ("admin", "admin"),  # Username trùng mật khẩu
    ("validUser", "StrongPass1!"),  # Hợp lệ
    ("invalid!", "Password1!"),  # Username chứa ký tự đặc biệt
]

for i, (user, pw) in enumerate(test_cases, 1):
    result = kiem_tra_tai_khoan(user, pw)
    print(f"Test case {i}: Username: {user}, Password: {pw} -> {result}")
