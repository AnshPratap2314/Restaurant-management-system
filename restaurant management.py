menu={
    'pizza': 199,
    'cold drinks':50,
    'hot coffee':30,
    'cold coffee': 80,
    'tea':20,
    'burger':60,
    'chaumeen':40,
    'patties':30,

}
print("Welcome to Royals Cafe")
print("Pizza: Rs199\nCold Drinks:Rs50\nHot Coffee:Rs30\nCold Coffee: Rs80Tea:Rs20\nBurger:Rs60\nChoumeen:Rs40\nPatties:Rs30\n")
order_total=0
item1=input("Enter the item name you want to order:")
if item1 in menu:
    order_total+=menu[item1]
    print(f"This item {item1} is added in your order")
else:
    print(f"Ordered item {item1} is not available yet")
another_order=input("do you want another thing? (yes/no) ")
if another_order == "yes":
    item2=input("enter another item name you want to order:")
    if item2 in menu:
        order_total+=menu[item2]
        print(f"This item {item2} is added to your order")
    else:
        print(f" This item {item2} is not available yet")
another_order2=input("do you want another thing? (yes/no) ")
if another_order2 == "yes":
    item3=input("enter another item name you want to order:")
    if item3 in menu:
        order_total+=menu[item3]
        print(f"This item {item3} is added to your order")
    else:
        print(f" This item {item3} is not available yet")
print(f"Total Amount you have to Pay:{order_total} ")