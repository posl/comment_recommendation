def main():
    N = int(input())
    total = 0.0
    for _ in range(N):
        x, u = input().split()
        x = float(x)
        if u == "JPY":
            total += x
        else:
            total += x * 380000.0
    print(total)

if __name__ == '__main__':
    main()