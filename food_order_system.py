# Restaurant Food Ordering System

menu = {
    "Main Course":{
        "Veg":{
            1:("Chilli Paneer",210),2:("Veg Biryani",250),
            3:("Kaju Curry",280),4:("Paneer Butter Masala",230)},
        "Non-Veg":{
            1:("Chicken Biryani",340),2:("Butter Chicken Masala",320),
            3:("Mutton Biryani",390),4:("Prawns Curry",370)}
    },
    "Starters":{
        "Veg":{
            1:("Paneer Tikka",220),2:("Baby Corn Manchurian",250),
            3:("Gobi Manchurian",210)},
        "Non-Veg":{
            1:("Chicken Majestic",340),2:("Chilli Chicken",320),
            3:("Mutton Kebab",390)}
    },
    "Rotis":{1:("Butter Naan",40),2:("Garlic Cheese Naan",50)},
    "Desserts":{1:("Apricot Delight",110),2:("Brownie",150),3:("Gulab Jamun",90)},
    "Soft Drinks":{1:("Coke",60),2:("Thumbs Up",50),3:("Juice",50)}
}

cart=[]

def show_items(items):
    for k,(n,p) in items.items():
        print(f"{k}. {n} - ₹{p}")
    ch=int(input("Select item (0 back): "))
    if ch==0:return
    if ch in items:
        qty=int(input("Quantity: "))
        n,p=items[ch]
        cart.append((n,p,qty))
        print("Added to cart.")
    else:
        print("Invalid choice")

def view_menu():
    cats=list(menu.keys())
    while True:
        print("\n--- MENU ---")
        for i,c in enumerate(cats,1):
            print(i,c)
        print("0 Back")
        ch=int(input("Choice: "))
        if ch==0:return
        if 1<=ch<=len(cats):
            sel=menu[cats[ch-1]]
            if isinstance(next(iter(sel.keys())),str):
                print("1. Veg\n2. Non-Veg")
                t=int(input("Choice: "))
                if t==1: show_items(sel["Veg"])
                elif t==2: show_items(sel["Non-Veg"])
            else:
                show_items(sel)

def show_cart():
    if not cart:
        print("Cart is empty.");return
    total=0
    for i,(n,p,q) in enumerate(cart,1):
        s=p*q
        total+=s
        print(f"{i}. {n} x{q} = ₹{s}")
    print("Total:",total)

def remove_item():
    if not cart:
        print("Cart empty");return
    show_cart()
    ch=int(input("Remove item no (0 cancel): "))
    if 1<=ch<=len(cart):
        cart.pop(ch-1)
        print("Removed.")

def bill():
    if not cart:
        print("Cart empty");return
    print("\n====== BILL ======")
    total=0
    for n,p,q in cart:
        s=p*q
        total+=s
        print(f"{n:25} {q} x {p} = ₹{s}")
    print("-"*35)
    print(f"Grand Total = ₹{total}")

while True:
    print("\nRestaurant Food Ordering System")
    print("1.View Menu\n2.Add Item\n3.Remove Item\n4.View Cart\n5.Generate Bill\n6.Exit")
    c=int(input("Enter choice: "))
    if c==1 or c==2:
        view_menu()
    elif c==3:
        remove_item()
    elif c==4:
        show_cart()
    elif c==5:
        bill()
    elif c==6:
        print("Thank you!")
        break
    else:
        print("Invalid choice")
