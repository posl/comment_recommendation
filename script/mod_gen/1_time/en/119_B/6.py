def main():
    N = int(input())
    sum = 0
    for i in range(N):
        x, u = map(str, input().split())
        x = float(x)
        if u == "JPY":
            sum += x
        else:
            sum += x * 380000.0
    print(sum)

if __name__ == '__main__':
    main()