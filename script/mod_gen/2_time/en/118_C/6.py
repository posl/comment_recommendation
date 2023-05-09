def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = a[0]
    for i in range(n-1):
        if a[i+1] >= ans:
            ans += 1
        else:
            ans += a[i+1]
    print(ans)

if __name__ == '__main__':
    main()