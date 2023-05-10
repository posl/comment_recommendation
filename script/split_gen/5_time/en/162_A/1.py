def main():
    n = int(input())
    if n % 10 == 7 or (n // 10) % 10 == 7 or (n // 100) % 10 == 7:
        print("Yes")
    else:
        print("No")
