def main():
    #N: park's size, K: pond's size
    N, K = map(int, input().split())
    #A: park's height
    A = [list(map(int, input().split())) for _ in range(N)]
    #B: cumulative sum of A
    B = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            B[i + 1][j + 1] = B[i + 1][j] + B[i][j + 1] - B[i][j] + A[i][j]
    
    #binary search
    #l: min height, r: max height
    l, r = 0, 10 ** 9
    while r - l > 1:
        m = (l + r) // 2
        #check if there's a pond with median height >= m
        if check(B, N, K, m):
            l = m
        else:
            r = m
    print(l)
