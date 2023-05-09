def main():
    N = int(input())
    money = 0
    for i in range(N):
        x, u = input().split()
        if u == "JPY":
            money += int(x)
        else:
            money += float(x) * 380000.0
    print(money)

if __name__ == '__main__':
    main()