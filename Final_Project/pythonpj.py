def get_input():
    """รับข้อมูลราคาทุน ราคาขาย และจำนวนที่ขาย"""
    cost_price = float(input("Enter cost price per unit / ราคาทุนต่อหน่วย: "))
    selling_price = float(input("Enter selling price per unit / ราคาขายต่อหน่วย: "))
    
    # รับ quantity
    quantity = float(input("Enter quantity sold / จำนวนสินค้าที่ขายได้: "))
    
    return cost_price, selling_price, quantity


def calculate_profit_loss(cost_price, selling_price, quantity):
    """คำนวณกำไรหรือขาดทุน"""
    total_cost = cost_price * quantity
    total_revenue = selling_price * quantity
    return total_revenue - total_cost


def display_profit_loss(profit_loss):
    """แสดงผลกำไรหรือขาดทุนสำหรับแต่ละรายการ"""
    if profit_loss > 0:
        print(f"You made a profit of: {profit_loss:.2f} baht / คุณได้กำไร: "
              f"{profit_loss:.2f} บาท")
    elif profit_loss < 0:
        print(f"You incurred a loss of: {abs(profit_loss):.2f} baht / คุณขาดทุน: "
              f"{abs(profit_loss):.2f} บาท")
    else:
        print("No profit or loss / ไม่มีทั้งกำไรหรือขาดทุน")


def display_total_summary(total_profit_loss):
    """แสดงผลรวมทั้งหมด"""
    print("\n--- Final Summary / สรุปผลรวม ---")
    if total_profit_loss > 0:
        print(f"Total Profit: {total_profit_loss:.2f} baht / กำไรรวม: "
              f"{total_profit_loss:.2f} บาท")
    elif total_profit_loss < 0:
        print(f"Total Loss: {abs(total_profit_loss):.2f} baht / ขาดทุนรวม: "
              f"{abs(total_profit_loss):.2f} บาท")
    else:
        print("No total profit or loss / ไม่มีทั้งกำไรหรือขาดทุน")


# เริ่มโปรแกรม
num_items = int(input("Enter the number of items to calculate / "
                      "กรอกจำนวนสินค้าที่ต้องการคำนวณ: "))
total_profit_loss = 0

for i in range(num_items):
    print(f"\nItem {i + 1} / สินค้า {i + 1}")
    
    # รับข้อมูล
    cost_price, selling_price, quantity = get_input()

    # ตรวจสอบว่าจำนวนสินค้าที่ขายได้ถูกต้องหรือไม่
    if quantity <= 0:
        print("Unable to calculate / ไม่สามารถคำนวณได้สำหรับสินค้านี้ ข้ามไปสินค้าถัดไป")
        continue  # ข้ามไปสินค้าถัดไป

    # คำนวณกำไรหรือขาดทุน
    profit_loss = calculate_profit_loss(cost_price, selling_price, quantity)

    # แสดงผลกำไรหรือขาดทุนของแต่ละสินค้า
    display_profit_loss(profit_loss)

    # สะสมกำไร/ขาดทุนทั้งหมด
    total_profit_loss += profit_loss

# แสดงผลสรุปสุดท้าย
display_total_summary(total_profit_loss)
