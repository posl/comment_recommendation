def problems130_b():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    count = 1
    for i in range(len(l)):
        d += l[i]
        if d <= x:
            count += 1
    print(count)

if __name__ == '__main__':
    problems130_b()