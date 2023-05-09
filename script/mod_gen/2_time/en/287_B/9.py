def main():
    #input
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    #compute
    s.sort()
    t.sort()
    ans = 0
    i = 0
    j = 0
    while i < n and j < m:
        if s[i] == t[j]:
            ans += 1
            i += 1
            j += 1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    #output
    print(ans)

if __name__ == '__main__':
    main()