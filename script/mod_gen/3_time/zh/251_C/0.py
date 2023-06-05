def main():
    n = int(input())
    d = {}
    for i in range(n):
        s, t = input().split()
        if s in d:
            if d[s][0] < int(t):
                d[s] = (int(t), i)
        else:
            d[s] = (int(t), i)
    ans = sorted(d.items(), key=lambda x: (x[1][0], -x[1][1]), reverse=True)
    print(ans[0][1][1] + 1)

if __name__ == '__main__':
    main()