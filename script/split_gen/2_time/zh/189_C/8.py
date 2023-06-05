def main():
    n,x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        V, P = map(int, input().split())
        v.append(V)
        p.append(P)
    alcohol = 0
    for i in range(n):
        alcohol += v[i] * p[i] / 100
        if alcohol > x:
            print(i + 1)
            return
    print(-1)
    return
