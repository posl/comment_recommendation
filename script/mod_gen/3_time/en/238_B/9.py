def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    upper = 180
    lower = 0
    for i in range(n):
        if a[i] <= upper and a[i] >= lower:
            upper = a[i] + 180
            lower = a[i]
        elif a[i] > upper:
            upper = upper + 360 - a[i]
            lower = a[i] - 180
        else:
            upper = a[i] + 180
            lower = lower - 360 + a[i]
    print(upper - 180)

if __name__ == '__main__':
    main()