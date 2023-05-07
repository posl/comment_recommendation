def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #print(a)
    #print(b)
    min_time = 10**18
    for i in range(n):
        time = 0
        for j in range(x):
            time += a[i] + b[i]*j
        if time < min_time:
            min_time = time
    print(min_time)
