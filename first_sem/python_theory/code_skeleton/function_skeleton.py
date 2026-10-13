# Complete the five functions below. Then complete the main program so it calls them 
# and prints the bill.

# get_price(item) returns the price of the item.
#  It returns 0 if the item is not on the menu.
# item_cost(item, qty) returns the cost of buying qty of an item.
#  It must use get_price().
# calculate_gst(amount, rate=0.05) returns the GST on the amount.
#  The rate is 5% unless another rate is given.
# generate_bill(subtotal, discount_percent=0)
#  returns three values: the discount, the GST 
# (calculated on the amount after the discount), and the final total.
# split_bill(total, people) returns two values: the whole rupees each person pays, 
#  and the rupees left over.


def get_price(item):
    if item == "idli":
        return 30
    elif item == "dosa":
<<<<<<< HEAD
        return 30
    elif item == "biriyani":
        return 50
    elif item == "coffee":
        return 20
    elif item == "chapati":
        return 30
    else:
         return 0

def item_cost(item, qty):
price=get_price(item)
return price * qty

  
def calculate_gst(amount, rate=0.05):      
     gst=amount * 0.05
     return round(gst,2)
pass  
=======
        return 50
    elif item == "tea":
        return 10
    elif item == "golibaje":
        return 40
    else:
        return 0


def item_cost(item, qty):
    # TODO: call get_price() and return the cost
    price=get_price(item)
    return price * qty


def calculate_gst(amount, rate=0.05):
    # TODO: return the GST rounded to 2 decimals
    gst=amount * rate
    return round(gst,2)
>>>>>>> 743780ae69c9e7a8bc790e8ef56c9bb34b2b2557


def generate_bill(subtotal, discount_percent=0):
    discount = subtotal * discount_percent
<<<<<<< HEAD
    amount_after_discount =subtotal - discount      
=======
    amount_after_discount = subtotal - discount
>>>>>>> 743780ae69c9e7a8bc790e8ef56c9bb34b2b2557
    gst = calculate_gst(amount_after_discount)
    total = amount_after_discount + gst
    return discount,gst,total


def split_bill(total, people):
<<<<<<< HEAD
    each_pays = total / people
=======
    each_pays = total / people   
>>>>>>> 743780ae69c9e7a8bc790e8ef56c9bb34b2b2557
    left_over = total % people
    return each_pays,left_over


# ---------------- Main program ----------------
# A group of 3 friends orders 2 dosa and 3 coffee, with a 10% coupon.

<<<<<<< HEAD
subtotal1 = item_cost('dosa',2) 
discount1, gst1, total1 = generate_bill(subtotal1,0.02)
subtotal2 = item_cost('coffee',3) 
discount2, gst2, total2 = generate_bill(subtotal2,0.02)

each, extra = split_bill(total1+total2,3)

print("Subtotal :", subtotal1)
print("Discount :", discount1)
print("GST      :", gst1)
print("Total    :", total1)
print("Subtotal :", subtotal2)
print("Discount :", discount2)
print("GST      :", gst2)
print("Total    :", total2)
=======
subtotal = item_cost('dosa',2)# TODO: call item_cost() for dosa and coffee and add them
discount, gst, total = # TODO: call generate_bill() using a KEYWORD argument
each, extra = # TODO: call split_bill() with the total (as a whole number) and 3 people
>>>>>>> 743780ae69c9e7a8bc790e8ef56c9bb34b2b2557

print("Each pays:", each, "| Left over:", extra)