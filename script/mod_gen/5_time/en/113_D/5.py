def path(H, W, K):
    if W == 1:
        return 1
    if K == 1:
        return path(H-1, W-1, K) + path(H-1, W-1, K+1)
    if K == W:
        return path(H-1, W-1, K) + path(H-1, W-1, K-1)
    return path(H-1, W-1, K-1) + path(H-1, W-1, K) + path(H-1, W-1, K+1)
H, W, K = map(int, input().split())
print(path(H, W, K) % 1000000007)

if __name__ == '__main__':
    path()