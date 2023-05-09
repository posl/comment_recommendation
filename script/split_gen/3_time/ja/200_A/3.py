def main():
    n = int(input())
    if n % 100 == 0:
        print(int(n / 100))
    else:
        print(int(n / 100 + 1))
