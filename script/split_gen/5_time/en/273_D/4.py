def main():
    h, w, r, c = map(int, input().split())
    n = int(input())
    rs = [0] * n
    cs = [0] * n
    for i in range(n):
        rs[i], cs[i] = map(int, input().split())
    q = int(input())
    ds = [0] * q
    ls = [0] * q
    for i in range(q):
        ds[i], ls[i] = input().split()
        ls[i] = int(ls[i])
    for i in range(q):
        if ds[i] == "L":
            c -= ls[i]
            for j in range(n):
                if rs[j] == r and cs[j] <= c:
                    c = cs[j] - 1
        elif ds[i] == "R":
            c += ls[i]
            for j in range(n):
                if rs[j] == r and cs[j] >= c:
                    c = cs[j] + 1
        elif ds[i] == "U":
            r -= ls[i]
            for j in range(n):
                if cs[j] == c and rs[j] <= r:
                    r = rs[j] - 1
        elif ds[i] == "D":
            r += ls[i]
            for j in range(n):
                if cs[j] == c and rs[j] >= r:
                    r = rs[j] + 1
        print(r, c)
