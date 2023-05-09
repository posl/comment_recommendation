def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        a, b = map(int, input().split())
        v.append(a)
        p.append(b)
    al = 0
    for i in range(n):
        al += v[i] * p[i]
        if al > x * 100:
            print(i + 1)
            break
    else:
        print(-1)
