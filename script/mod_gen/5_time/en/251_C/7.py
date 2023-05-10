def solve():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        ss, tt = input().split()
        s.append(ss)
        t.append(int(tt))
    for i in range(n):
        if s[i] == s[i+1]:
            t[i+1] = t[i]
    print(t.index(max(t))+1)

if __name__ == '__main__':
    solve()