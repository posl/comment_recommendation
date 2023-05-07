def main():
    n = int(input())
    w = [int(x) for x in input().split()]
    s1 = w[0]
    s2 = sum(w[1:])
    ans = abs(s1 - s2)
    for i in range(1, n - 1):
        s1 += w[i]
        s2 -= w[i]
        ans = min(ans, abs(s1 - s2))
    print(ans)

if __name__ == '__main__':
    main()