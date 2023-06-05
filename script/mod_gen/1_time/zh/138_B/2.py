def problems138_b():
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    for i in a:
        result += 1/i
    print(1/result)
problems138_b()
