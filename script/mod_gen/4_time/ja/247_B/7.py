def solve():
    N = int(input())
    s = []
    t = []
    for _ in range(N):
        a, b = input().split()
        s.append(a)
        t.append(b)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                return "Yes"
    return "No"
print(solve())

if __name__ == '__main__':
    solve()