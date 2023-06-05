def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    a.append(a[1])
    s = sum(a[:3])
    ans = s
    for i in range(n-3):
        s += a[i+3]
        s -= a[i]
        ans = max(ans, s)
    print(ans)

if __name__ == '__main__':
    main()