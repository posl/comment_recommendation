def main():
    N, K = map(int, input().split())
    p = 0
    for i in range(1, N+1):
        if i >= K:
            p += 1
            continue
        j = i
        while j < K:
            j *= 2
            p += 1
    print(p/(N*2**(p-1)))
