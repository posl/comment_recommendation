def buy_sweets():
    n = int(input())
    if n % 4 == 0 or n % 7 == 0 or n % 11 == 0:
        print("Yes")
        return
    for i in range(1, n // 4 + 1):
        for j in range(1, n // 7 + 1):
            if n - 4 * i - 7 * j == 0:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    buy_sweets()