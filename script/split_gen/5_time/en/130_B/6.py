def problems130_b():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = [0]
    for i in range(1, n + 1):
        d.append(d[i - 1] + l[i - 1])
    print(sum([1 for i in d if i <= x]))
