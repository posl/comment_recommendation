def amidakuji(H, W, K):
    if H == 1:
        return 1
    if K == 1:
        return amidakuji(H-1, W, K) + amidakuji(H-1, W, K+1)
    if K == W:
        return amidakuji(H-1, W, K-1) + amidakuji(H-1, W, K)
    return amidakuji(H-1, W, K-1) + amidakuji(H-1, W, K) + amidakuji(H-1, W, K+1)

if __name__ == '__main__':
    amidakuji()