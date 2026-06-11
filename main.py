employees = [
    {
        "id": "NV001",
        "name": "Nguyen Van A",
        "basic_salary": 400000,
        "work_days": 25,
        "allowance": 1500000,
        "sum_salary": 11500000,
        "rank": "Trung bình"
    }
]
#KT SỐ NGUYÊN DƯƠNG
def validate_num(num):
    return num > 0
#Validate rỗng
def validate_emty(input_emty):
    if input_emty.strip() == "":
        return True
    return False
#Validate id nhân viên
def validate_id(id_emp):
    for index,emp in enumerate(employees):
        if id_emp == emp["id"]:
            return index
    return -1

#Hiện thị nhân viên
def show_employ():
    if employees == []:
        print("Hiện tại danh sách nhân viên đang trống")
    else:
        print("--- Danh sách nhân viên hiện tại ---")
        for index, emp in enumerate(employees, start=1):
            print(f"{index}. Mã nhân viên: {emp["id"]} | Tên nhân viên: {emp["name"]} | Lương ngày: {emp["basic_salary"]} | Số ngày công: {emp["work_days"]} | Phụ cấp: {emp["allowance"]} | Tổng thu nhập: {emp["sum_salary"]} | Phân loại thu nhập: {emp["rank"]}")

#Phân loại thu nhập
def rank_input(total_salary):
    eval_total = ""
    if total_salary >= 30000000:
        eval_total = "Cao"
    elif total_salary >= 15000000:
        eval_total = "Khá"
    elif total_salary >= 9000000:
        eval_total = "Trung bình"
    else:
        eval_total = "Thấp"
    return eval_total
#Thêm nhân viên
def add_employ():
    id_emp = input("Nhập mã nhân viên mới: ").strip().upper()
    if validate_id(id_emp) != -1:
        print("Mã nhân viên đã tồn tại")
    else:
        while True:
            name_emp = input("Nhập tên nhân viên mới: ").strip().title()
            if validate_emty(name_emp):
                print("Vui lòng nhập tên nhân viên!")
            else:
                while True:
                    try:
                        salary_day = int(input("Nhập lương 1 ngày của nhân viên: "))
                        day_work = int(input("Nhập số ngày công: "))
                        more_money = int(input("Nhập phụ cấp: "))
                        
                        if validate_num(salary_day) and validate_num(day_work) and validate_num(more_money):
                            break
                        print("Vui lòng nhập lại")
                        
                    except ValueError:
                        print("Vui lòng nhập số nguyên")
                total = (salary_day * day_work) + more_money
                eval_total = rank_input(total)
                employees.append({
                    "id": id_emp,
                    "name": name_emp,
                    "basic_salary": salary_day,
                    "work_days": day_work,
                    "allowance": more_money,
                    "sum_salary": total,
                    "rank": eval_total
                })
                print("Đã thêm thành công")
                break
            
#Cập nhật thông tin
def update_infor():
    id_emp = input("Nhập mã nhân viên cần cập nhật: ").strip().upper()
    idx = validate_id(id_emp)
    if validate_id(id_emp) == -1:
        print("Mã nhân viên không tồn tại")
    else:
        while True:
            try:
                salary_day = int(input("Nhập lương 1 ngày mới của nhân viên: "))
                day_work = int(input("Nhập số ngày công mới: "))
                more_money = int(input("Nhập phụ cấp mới: "))
                
                if validate_num(salary_day) and validate_num(day_work) <= 31 and validate_num(more_money):
                    break
                print("Vui lòng nhập lại")
                
            except ValueError:
                print("Vui lòng nhập số nguyên")
        employees[idx]["basic_salary"] = salary_day
        employees[idx]["work_days"] = day_work
        employees[idx]["allowance"] = more_money
        total = (salary_day * day_work) + more_money
        employees[idx]["sum_salary"] = total
        eval_total = rank_input(total)
        employees[idx]["rank"] = eval_total
        print("Cập nhật thành công")
        
def delete_employ():
    id_emp = input("Nhập mã nhân viên cần xóa: ").strip().upper()
    idx = validate_id(id_emp)
    if validate_id(id_emp) == -1:
        print("Mã nhân viên không tồn tại")
    else:
        while True:
            confirm = input("Bạn có xác nhận muốn xóa(Y/N): ").strip().upper()
            if confirm == "Y":
                employees.pop(idx)
                print("Đã xóa nhân viên đó")
                break
            elif confirm == "N":
                print("Hủy xóa nhân viên")
                break
            else:
                print("Vui lòng nhập Y hoặc N")
   
#Tìm nhân viên
def find_employ():
    id_emp = input("Nhập mã nhân viên cần tìm: ").strip().upper()
    idx = validate_id(id_emp)
    if validate_id(id_emp) == -1:
        print("Mã nhân viên không tồn tại")
    else:
        print(f"Tìm thấy nhân viên có mã là {id_emp}:")      
        print(f"Mã nhân viên: {employees[idx]["id"]} | Tên nhân viên: {employees[idx]["name"]} | Lương ngày: {employees[idx]["basic_salary"]} | Số ngày công: {employees[idx]["work_days"]} | Phụ cấp: {employees[idx]["allowance"]} | Tổng thu nhập: {employees[idx]["sum_salary"]} | Phân loại thu nhập: {employees[idx]["rank"]}")    

#Thống kê lại
def month_end_statistics():
    print("--- Bảng thống kê nhân viên cuối tháng ---")
    count_emp_high_salary = 0
    count_emp_rather_salary = 0
    count_emp_avg_salary = 0
    count_emp_low_salary = 0
    for emp in employees:
        eval_emp = rank_input(emp["sum_salary"])
        if eval_emp == "Cao":
            count_emp_high_salary += 1
        elif eval_emp == "Khá":
            count_emp_rather_salary += 1
        elif eval_emp == "Trung bình":
            count_emp_avg_salary += 1
        elif eval_emp == "Thấp":
            count_emp_low_salary += 1
            
    print(f"Số lượng nhân viên thuộc nhóm thu nhập CAO là: {count_emp_high_salary}")
    print(f"Số lượng nhân viên thuộc nhóm thu nhập KHÁ là: {count_emp_rather_salary}")
    print(f"Số lượng nhân viên thuộc nhóm thu nhập TRUNG BÌNH là: {count_emp_avg_salary}")
    print(f"Số lượng nhân viên thuộc nhóm thu nhập THẤP là: {count_emp_low_salary}")
    
def main():
    while True:
        print("""=== HỆ THỐNG QUẢN LÝ NHÂN VIÊN ===
              1. Hiện thị danh sách nhân viên
              2. Tiếp nhận nhân viên mới
              3. Cập nhật thông tin và ngày công
              4. Xóa nhân viên
              5. Tìm kiếm nhân viên
              6. Thống kê quỹ lương và nhân sự
              7. Thoát chương trình
              """)
        
        while True:
            try:
                choice = int(input("Nhập lựa chọn của bạn: "))
                
                if 1 <= choice <= 7:
                    break
                print("Chỉ nhập lựa chọn trong khoảng 1 - 8") 
                
            except ValueError:
                print("Vui lòng chỉ nhập lựa chọn từ 1 - 8")
        
        match choice:
            case 1:
                show_employ()
            case 2:
                add_employ()
            case 3:
                update_infor()
            case 4:
                delete_employ()
            case 5:
                find_employ()
            case 6:
                month_end_statistics()
            case 7:
                print("Thoát chương trình")
                break
        
if __name__ == "__main__":
    main()