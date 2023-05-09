def main():
    N = int(input())
    d = {}
    for i in range(N):
        L, R = map(int, input().split())
        if L in d:
            if R in d:
                if d[L] > d[R]:
                    d[L] = d[R]
                else:
                    d[R] = d[L]
            else:
                d[R] = d[L]
        else:
            if R in d:
                d[L] = d[R]
            else:
                d[L] = L
                d[R] = L
    
    d = sorted(d.items())
    #print(d)
    ans = []
    i = 0
    while i < len(d):
        if i == len(d) - 1:
            ans.append(d[i][1])
            break
        if d[i][1] == d[i+1][1]:
            ans.append(d[i][1])
            i += 1
        else:
            ans.append(d[i][1])
        i += 1
    #print(ans)
    for i in range(0, len(ans), 2):
        print(ans[i], ans[i+1])

if __name__ == '__main__':
    main()