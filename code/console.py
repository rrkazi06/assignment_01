"""
console.py — the *console* (terminal) interface for the Bill Splitter.

It reads a few values from the keyboard, calls the functions in bill.py to do the
math, and prints the results. All the real work lives in bill.py — this file just
handles input and output.
"""

from bill import tip_amount, grand_total, split_evenly, is_generous

subtotal = float(input("Bill subtotal: "))
pct = float(input("Tip percent: "))
people = int(input("Number of people: "))

tip = tip_amount(subtotal, pct)
total = grand_total(subtotal, pct)
per_person = split_evenly(total, people)

print(f"Tip ({pct:.0f}%): ${tip:.2f}")
print(f"Grand total: ${total:.2f}")
print(f"Per person ({people}): ${per_person:.2f}")
if is_generous(pct):
    print("That's a generous tip! 🎉")
