def main():
    n, m = map(int, input().split())
    p = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(m):
        x, y = input().split()
        x = int(x)
        if s[x] == 0:
            s[x] = y
            if s[x] == "AC":
                p[x] = 1
            else:
                p[x] = 0
    print(sum(p), s.count("WA") - sum(p))
