def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    a.append(a[1])
    for i in range(n):
        a[i] += a[i+1]
    a.append(a[2])
    ans = 0
    for i in range(n):
        ans = max(ans, min(a[i], a[i+n]))
    print(ans)

if __name__ == '__main__':
    main()