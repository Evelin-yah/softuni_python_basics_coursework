tabs = int(input())
salary = float(input())
penalty = 0
for tab in range(tabs):
    text = input()
    if text == "Facebook":
        penalty += 150
    elif text == "Instagram":
        penalty += 100
    elif text == "Reddit":
        penalty += 50
left_money = salary - penalty
if left_money <= 0:
    print("You have lost your salary.")
else:
    print(f"{int(left_money)}")