def main():
    N,K = map(int,input().split())
    if K%2 == 0:
        k = K//2
        if N >= k:
            n = N//k
            if N%k >= k//2:
                n += 1
        else:
            n = 0
    else:
        k = K
        if N >= k:
            n = N//k
            if N%k >= k//2:
                n += 1
        else:
            n = 0
    print(n**3)
