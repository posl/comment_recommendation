def solve():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = input().split()
        s.append(a)
        t.append(b)
    #print(s)
    #print(t)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == t[j]:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    solve()