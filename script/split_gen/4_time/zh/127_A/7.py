def main():
    age, price = map(int, input().split())
    if age >= 13:
        print(price)
    elif age >= 6:
        print(price//2)
    else:
        print(0)
