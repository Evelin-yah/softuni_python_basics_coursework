lili_age = int(input())
laundry_price = float(input())
price_per_toy = int(input())
money_gift = 0
toy_gift = 0
for birthday in range(1, lili_age + 1):
    if birthday % 2 == 0:
        money_gift += 10 * birthday / 2-1
    else:
        toy_gift += 1
money_from_toys = toy_gift * price_per_toy
total_money = money_gift + money_from_toys
diff = abs(total_money - laundry_price)
if total_money >= laundry_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")