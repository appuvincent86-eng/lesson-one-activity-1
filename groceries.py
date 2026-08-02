print("======== Grocery List ========\n")



low_price_items=0
medium_price_items=0
high_price_items=0

customers_served=0
total_sales=0

billing=True

while billing:
    name=input("Enter the name of the customer: ")
    item_count=int(input(f"Hello {name}, enter how many things are you buying: "))

    if item_count <= 0:
        print("You must buy at least one item.\n")
        continue

print(f"\nbilling item list for {name}:")
customer_total=0
item_number=1

while item_number <= item_count:
    item_name=input(f"Enter the name of item")
    price=int(input(f"Enter the price of"))
    quantity=int(input(f"Enter the quantity of" ))

    if price <=0:
        print("Price must be greater than zero.\n")
        continue

item_total=price*quantity
print(f"  {item_name}: {quantity} x {price} = {item_total}")

customer_total += item_total

if price < 50:
        low_price_items += quantity
elif price < 100:
        medium_price_items += quantity
else:
        high_price_items += quantity

item_number += 1

customers_served += 1
total_sales += customer_total
print(f"\nTotal bill for {name}: {customer_total}")
print(" billing complete.\n")

again=input("next customer yes/no: "). strip().lower()

if again != "yes":
    billing=False



    print("\n======== report ========")
