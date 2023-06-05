def solve():
    n = int(input())
    ss = []
    ts = []
    for i in range(n):
        s, t = input().split()
        ss.append(s)
        ts.append(t)
    #print(ss, ts)
    for i in range(n):
        if ss[i] == ts[i]:
            print('No')
            return
    for i in range(n):
        for j in range(i+1, n):
            if ss[i] == ts[j] and ss[j] == ts[i]:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    solve()