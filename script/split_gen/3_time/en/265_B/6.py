def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    x = [0] * m
    y = [0] * m
    for i in range(m):
        x[i], y[i] = map(int, input().split())
    time = t
    for i in range(n-1):
        time -= a[i]
        if time <= 0:
            print('No')
            return
        for j in range(m):
            if i+1 == x[j]:
                time += y[j]
                break
    print('Yes')
