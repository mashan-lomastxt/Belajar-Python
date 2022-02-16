from itertools import count

days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
for i, j in zip(count(), days):
    if i == 0:
        print("Working Days")
    if i == 5:
        print("\nHoliday..!!!")
    if i == 5 and i == 6:
        print(j)
    else:
        print(j)