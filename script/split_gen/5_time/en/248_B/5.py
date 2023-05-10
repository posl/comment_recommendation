def problems248_b():
    a, b, k = map(int, input().split())
    count = 0
    while b // a > 0:
        a *= k
        count += 1
    print(count)
