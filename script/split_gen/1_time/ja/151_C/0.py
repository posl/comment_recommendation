def main():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        a, b = input().split()
        p.append(int(a))
        s.append(b)
    ac = [0] * n
    wa = [0] * n
    for i in range(m):
        if s[i] == "AC":
            ac[p[i]-1] = 1
        else:
            if ac[p[i]-1] == 0:
                wa[p[i]-1] += 1
    ans1 = 0
    ans2 = 0
    for i in range(n):
        if ac[i] == 1:
            ans1 += 1
            ans2 += wa[i]
    print(ans1, ans2)
