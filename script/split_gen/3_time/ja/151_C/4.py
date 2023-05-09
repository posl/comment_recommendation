def main():
    n, m = map(int, input().split())
    p = []
    s = []
    for i in range(m):
        pi, si = input().split()
        p.append(pi)
        s.append(si)
    print(p)
    print(s)
