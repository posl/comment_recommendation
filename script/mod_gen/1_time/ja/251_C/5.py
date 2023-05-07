def main():
    N = int(input())
    d = {}
    for i in range(N):
        s, t = input().split()
        t = int(t)
        if s not in d:
            d[s] = [t, i]
        else:
            if d[s][0] < t:
                d[s] = [t, i]
    ans = 10**5
    for i in d.values():
        ans = min(ans, i[1])
    print(ans+1)

if __name__ == '__main__':
    main()