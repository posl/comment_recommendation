def problem127_a():
    age, price = map(int, input().split())
    if age >= 13:
        print(price)
    elif age >= 6 and age <= 12:
        print(price // 2)
    else:
        print(0)
