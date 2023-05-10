def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    ans = 0
    for i in range(n):
        if a[i] > max:
            max = a[i]
        else:
            ans += max - a[i]
    print(ans)

if __name__ == '__main__':
    main()