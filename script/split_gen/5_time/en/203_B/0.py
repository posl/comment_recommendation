def problem203_b():
    n, k = map(int, input().split())
    sum = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            sum += i*100 + j
    print(sum)
