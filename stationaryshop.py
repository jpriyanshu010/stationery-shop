import tkinter as tk
from tkinter import messagebox

menu = {
    "Pen": 10,
    "Pencil": 5,
    "Notebook": 50,
    "Eraser": 3,
    "Scale": 15
}

cart = {}
total = 0

def add_item():
    global total

    item = item_var.get()
    qty = qty_entry.get()

    if item == "Select Item":
        messagebox.showerror("Error", "Please select an item.")
        return

    if not qty.isdigit() or int(qty) <= 0:
        messagebox.showerror("Error", "Enter a valid quantity.")
        return

    qty = int(qty)
    cost = menu[item] * qty
    total += cost

    if item in cart:
        cart[item]["qty"] += qty
        cart[item]["cost"] += cost
    else:
        cart[item] = {
            "qty": qty,
            "price": menu[item],
            "cost": cost
        }

    bill_box.insert(tk.END,
                    f"{item}   Qty:{qty}   Rs {cost}\n")

    total_label.config(text=f"Total: Rs {total}")

    qty_entry.delete(0, tk.END)


def generate_bill():
    bill = "\n------ FINAL BILL ------\n"

    for item, details in cart.items():
        bill += f"{item}  x{details['qty']} = Rs {details['cost']}\n"

    bill += f"\nGrand Total = Rs {total}"

    messagebox.showinfo("Bill", bill)


root = tk.Tk()
root.title("Priyanshu Stationary Shop")
root.geometry("500x500")

tk.Label(root,
         text="Priyanshu Stationary Shop",
         font=("Arial", 18, "bold")).pack(pady=10)

item_var = tk.StringVar()
item_var.set("Select Item")

option = tk.OptionMenu(root, item_var, *menu.keys())
option.pack()

tk.Label(root, text="Quantity").pack()

qty_entry = tk.Entry(root)
qty_entry.pack()

tk.Button(root,
          text="Add Item",
          command=add_item,
          bg="green",
          fg="white").pack(pady=10)

bill_box = tk.Text(root, height=12, width=45)
bill_box.pack()

total_label = tk.Label(root,
                       text="Total: Rs 0",
                       font=("Arial", 14))
total_label.pack(pady=5)

tk.Button(root,
          text="Generate Bill",
          command=generate_bill,
          bg="blue",
          fg="white").pack(pady=10)

root.mainloop()
