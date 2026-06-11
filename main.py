employees = [
    {
        "id": "NV001",
        "name": "Nguyen Van A",
        "basic_salary": 400000,
        "work_days": 25,
        "allowance": 1500000,
        "sum_salary": 11500000,
        "rank": "Khá"
    }
]

def show_employ():
    if employees == []:
        print("Hiện tại danh sách nhân viên đang trống")
    else:
        print("--- Danh sách nhân viên hiện tại ---")
        for index, emp in enumerate(employees, start=1):
            print(f"{index}. Mã nhân viên: {emp["id"]} | Tên nhân viên: {emp["name"]} | Lương ngày: {emp["basic_salary"]} | Số ngày công: {emp["work_days"]} | Phụ cấp: {emp["allowance"]} | Tổng thu nhập: {emp["sum_salary"]} | Phân loại thu nhập: {emp["rank"]}")
def main():
    while True:
        print("""=== HỆ THỐNG QUẢN LÝ NHÂN VIÊN ===
              1. Hiện thị danh sách nhân viên
              2. Tiếp nhận nhân viên mới
              3. Cập nhật thông tin và ngày công
              4. Xóa nhân viên
              5. Tìm kiếm nhân viên
              6. Thống kê quỹ lương và nhân sự
              7. Phân loại thu nhập tự động
              8. Thoát chương trình
              """)
        
        while True:
            try:
                choice = int(input("Nhập lựa chọn của bạn: "))
                
                if 1 <= choice <= 8:
                    break
                print("Chỉ nhập lựa chọn trong khoảng 1 - 8") 
                
            except ValueError:
                print("Vui lòng chỉ nhập lựa chọn từ 1 - 8")
        
        match choice:
            case 1:
                show_employ()
            case 8:
                print("Thoát chương trình")
                break
        
if __name__ == "__main__":
    main()