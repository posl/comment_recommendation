def main():
    N = int(input())
    total = 0
    for i in range(N):
        x, u = map(str, input().split())
        if u == "JPY":
            total += int(x)
        else:
            total += float(x) * 380000.0
    print(total)
main()

if __name__ == '__main__':
    main()