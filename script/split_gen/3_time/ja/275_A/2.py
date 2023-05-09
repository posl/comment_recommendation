def problems275_a():
    n = int(input())
    h = list(map(int, input().split()))
    max = 0
    for i in range(n):
        if h[i] > max:
            max = h[i]
            max_index = i
    print(max_index+1)
