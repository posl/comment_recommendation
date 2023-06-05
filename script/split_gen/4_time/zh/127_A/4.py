def main():
    age, fee = map(int, input().split())
    if age >= 13:
        print(fee)
    elif age >= 6:
        print(fee // 2)
    else:
        print(0)
