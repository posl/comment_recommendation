def main():
    num = int(input())
    if num % 10 == 7 or num // 10 % 10 == 7 or num // 100 == 7:
        print("Yes")
    else:
        print("No")
