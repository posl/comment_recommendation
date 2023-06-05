def main():
    n, m = map(int, input().split())
    p = [0 for i in range(n)]
    s = ["" for i in range(n)]
    for i in range(m):
        x, y = map(str, input().split())
        p[int(x) - 1] += 1
        s[int(x) - 1] = y
    ac = 0
    wa = 0
    for i in range(n):
        if s[i] == "AC":
            ac += 1
            wa += p[i]
        else:
            p[i] = 0
    print(ac, wa)
