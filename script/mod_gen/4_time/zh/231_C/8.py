def main():
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    for i in range(q):
        ans = 0
        for j in range(n):
            if a[j] >= x[i]:
                ans += 1
        print(ans)

if __name__ == '__main__':
    main()