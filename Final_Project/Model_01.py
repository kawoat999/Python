# Get the number of items to calculate profit or loss
# รับข้อมูลจำนวนสินค้าที่ต้องการคำนวณกำไรขาดทุน
num_items = int(input("Enter the number of items to calculate: "))

# Use a for loop to calculate for multiple items
# ใช้ for loop ในการคำนวณหลายรายการ
for i in range(num_items):
    print(f"\nItem {i+1}")
    # แสดงรายการที่กำลังคำนวณ
    
    # Get the cost price, selling price, and quantity
    # รับข้อมูลราคาทุน, ราคาขาย และจำนวนสินค้า
    cost_price = float(input("Enter the cost price per unit: "))
    selling_price = float(input("Enter the selling price per unit: "))
    quantity = int(input("Enter the quantity sold: "))

    # Calculate total cost and total revenue
    # คำนวณต้นทุนรวมและรายได้รวม
    total_cost = cost_price * quantity
    total_revenue = selling_price * quantity

    # Calculate profit or loss
    # คำนวณกำไรหรือขาดทุน
    profit_loss = total_revenue - total_cost

    # Display the result indicating profit or loss
    # แสดงผลลัพธ์ว่ามีกำไรหรือขาดทุน
    if profit_loss > 0:
        print(f"You made a profit of: {profit_loss} baht")
        # คุณได้กำไร
    elif profit_loss < 0:
        print(f"You incurred a loss of: {abs(profit_loss)} baht")
        # คุณขาดทุน
    else:
        print("No profit or loss")
        # ไม่มีทั้งกำไรและขาดทุน
