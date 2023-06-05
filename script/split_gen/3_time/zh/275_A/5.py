def problems275_a():
    n = int(input())
    H = list(map(int, input().split()))
    maxH = max(H)
    for i in range(n):
        if H[i] == maxH:
            print(i+1)
            break
