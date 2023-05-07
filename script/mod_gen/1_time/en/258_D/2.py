def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        v1, v2 = map(int, input().split())
        a.append(v1)
        b.append(v2)
    min_time = min(a)
    time = 0
    for i in range(n):
        time += a[i] + b[i]
    x -= n
    time += min_time * x
    print(time)

if __name__ == '__main__':
    main()