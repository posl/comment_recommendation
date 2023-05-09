def main():
    n = int(input())
    s = []
    t = []
    for _ in range(n):
        st = input().split()
        s.append(st[0])
        t.append(int(st[1]))
    ans = 0
    for i in range(n):
        if s[:i].count(s[i]) == 0:
            if ans == 0:
                ans = i
            elif t[ans] < t[i]:
                ans = i
    print(ans+1)
