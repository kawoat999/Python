def calculate_results():
    # รับข้อมูลราคาขายสินค้า, ราคาทุน และจำนวนสินค้าที่ขายจากผู้ใช้

    # รับราคาขายสินค้าชิ้นที่ 1, 2, และ 3
    sale_price_item_1 = float(input("Enter sale price of item 1: (กรอกราคาขายสินค้าชิ้นที่ 1): "))
    sale_price_item_2 = float(input("Enter sale price of item 2: (กรอกราคาขายสินค้าชิ้นที่ 2): "))
    sale_price_item_3 = float(input("Enter sale price of item 3: (กรอกราคาขายสินค้าชิ้นที่ 3): "))

    # รับราคาทุนสินค้าชิ้นที่ 1, 2, และ 3
    cost_price_item_1 = float(input("Enter cost price of item 1: (กรอกราคาทุนสินค้าชิ้นที่ 1): "))
    cost_price_item_2 = float(input("Enter cost price of item 2: (กรอกราคาทุนสินค้าชิ้นที่ 2): "))
    cost_price_item_3 = float(input("Enter cost price of item 3: (กรอกราคาทุนสินค้าชิ้นที่ 3): "))

    # รับจำนวนสินค้าที่ขายได้สำหรับชิ้นที่ 1, 2, และ 3
    quantity_item_1 = int(input("Enter quantity sold of item 1: (กรอกจำนวนสินค้าที่ขายได้ชิ้นที่ 1): "))
    quantity_item_2 = int(input("Enter quantity sold of item 2: (กรอกจำนวนสินค้าที่ขายได้ชิ้นที่ 2): "))
    quantity_item_3 = int(input("Enter quantity sold of item 3: (กรอกจำนวนสินค้าที่ขายได้ชิ้นที่ 3): "))

    # คำนวณต้นทุนรวมและยอดขายรวมของสินค้าแต่ละชนิด
    total_cost_item_1 = cost_price_item_1 * quantity_item_1  # ต้นทุนรวมสินค้าชิ้นที่ 1
    total_cost_item_2 = cost_price_item_2 * quantity_item_2  # ต้นทุนรวมสินค้าชิ้นที่ 2
    total_cost_item_3 = cost_price_item_3 * quantity_item_3  # ต้นทุนรวมสินค้าชิ้นที่ 3

    total_sales_item_1 = sale_price_item_1 * quantity_item_1  # ยอดขายรวมสินค้าชิ้นที่ 1
    total_sales_item_2 = sale_price_item_2 * quantity_item_2  # ยอดขายรวมสินค้าชิ้นที่ 2
    total_sales_item_3 = sale_price_item_3 * quantity_item_3  # ยอดขายรวมสินค้าชิ้นที่ 3

    # คำนวณต้นทุนรวมทั้งหมดและยอดขายรวมทั้งหมด
    total_cost = total_cost_item_1 + total_cost_item_2 + total_cost_item_3
    total_sales = total_sales_item_1 + total_sales_item_2 + total_sales_item_3

    # คำนวณกำไร
    profit = total_sales - total_cost

    # แสดงผลลัพธ์ทั้งภาษาอังกฤษและภาษาไทย
    output = (
        f"\nTotal cost: {total_cost:.2f} baht (ต้นทุนรวมทั้งหมด)\n"
        f"Total sales: {total_sales:.2f} baht (ยอดขายรวมทั้งหมด)\n"
        f"Total profit: {profit:.2f} baht (กำไรรวมทั้งหมด)\n"
    )

    print(output)

    # บันทึกผลลัพธ์ลงในไฟล์
    with open("results.txt", "w", encoding="utf-8") as file:
        file.write(output)

    print("Results have been saved to 'results.txt'")

def main_menu():
    while True:
        # พิมพ์กรอบเมนู
        print("\n" + "="*30)
        print(" " * 7 + "MAIN MENU" + " " * 7)
        print("="*30)
        print("1. Calculate Results")
        print("2. Exit")
        print("="*30)

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            calculate_results()
        elif choice == "2":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# เริ่มต้นโปรแกรม
if __name__ == "__main__":
    main_menu()
