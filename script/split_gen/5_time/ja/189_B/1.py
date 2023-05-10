def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        v_p = list(map(int, input().split()))
        v.append(v_p[0])
        p.append(v_p[1])
    sum = 0
    for i in range(n):
        sum += v[i] * p[i] / 100
        if sum > x:
            print(i + 1)
            return
    print(-1)
