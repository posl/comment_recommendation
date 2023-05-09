def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if a[n-i-1] == 1:
            for j in range(2*(n-i-1)+1, n+1, n-i-1):
                a[j-1] = 1 - a[j-1]
            ans.append(n-i)
    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()