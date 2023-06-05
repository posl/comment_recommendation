def main():
    n,m,q = map(int, input().split())
    l = [0] * m
    r = [0] * m
    for i in range(m):
        l[i], r[i] = map(int, input().split())
    p = [0] * q
    q = [0] * q
    for i in range(q):
        p[i], q[i] = map(int, input().split())
    for i in range(q):
        count = 0
        for j in range(m):
            if l[j] >= p[i] and r[j] <= q[i]:
                count += 1
        print(count)
