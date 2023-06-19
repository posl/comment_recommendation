def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i == 0:
            ans = a[0]
        else:
            ans = (ans + a[i]) / 2
    print(ans)

if __name__ == '__main__':
    main()