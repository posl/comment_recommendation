def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if a[i] < i+1:
            continue
        ans += a[i] - (i+1)
    print(ans)
main()

if __name__ == '__main__':
    main()