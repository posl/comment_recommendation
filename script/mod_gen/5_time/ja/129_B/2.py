def main():
    n = int(input())
    w = list(map(int, input().split()))
    s = sum(w)
    ans = s
    s1 = 0
    s2 = 0
    for t in range(1, n):
        s1 += w[t-1]
        s2 = s - s1
        ans = min(ans, abs(s1 - s2))
    print(ans)

if __name__ == '__main__':
    main()