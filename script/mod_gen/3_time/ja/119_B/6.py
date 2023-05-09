def main():
    N = int(input())
    sum = 0
    for _ in range(N):
        x, u = map(str, input().split())
        if u == "JPY":
            sum += int(x)
        else:
            sum += float(x) * 380000.0
    print(sum)

if __name__ == '__main__':
    main()