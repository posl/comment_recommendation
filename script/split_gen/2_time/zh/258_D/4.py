def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    min_time = 1000000000000000000
    for i in range(n):
        time = 0
        for j in range(n):
            time += a[j] + b[j]
        if time < min_time:
            min_time = time
    print(min_time)
