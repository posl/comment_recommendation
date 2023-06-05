def main():
    n = int(input())
    d = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s not in d:
            d[s] = [t, i]
        else:
            if d[s][0] < t:
                d[s] = [t, i]
    max_score = 0
    ans = 0
    for k, v in d.items():
        if v[0] > max_score:
            max_score = v[0]
            ans = v[1]
    print(ans+1)

if __name__ == '__main__':
    main()