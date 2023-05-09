def solve():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = map(int, input().split())
        s.append([a, b])
    for i in range(n):
        a, b = map(int, input().split())
        t.append([a, b])
    #print(s)
    #print(t)
    s.sort()
    t.sort()
    #print(s)
    #print(t)
    for i in range(n):
        if s[i][0] != t[i][0] or s[i][1] != t[i][1]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    solve()