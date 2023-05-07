def main():
    N = int(input())
    yen = 0
    btc = 0
    for i in range(N):
        x, u = input().split()
        if u == "JPY":
            yen += int(x)
        else:
            btc += float(x)
    print(yen + btc * 380000)

if __name__ == '__main__':
    main()