def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if a[i] + 1 == a[i+1]:
            ans += 1
        else:
            ans = 0
    if ans == 0:
        print(0)
    else:
        print(ans+1)

if __name__ == '__main__':
    main()