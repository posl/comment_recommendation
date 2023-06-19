def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(a[0]):
        t = 0
        for j in range(n):
            t += i % a[j]
        ans = max(ans, t)
    print(ans)

if __name__ == '__main__':
    main()