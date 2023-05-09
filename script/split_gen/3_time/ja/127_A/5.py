def main():
    age, fee = map(int, input().split())
    if age < 6:
        print(0)
    elif age < 13:
        print(fee // 2)
    else:
        print(fee)
