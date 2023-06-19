def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    # 从左到右扫描，找到最小的A_x
    x = 0
    for i in range(1, N):
        if A[i] < A[x]:
            x = i
    # 从右到左扫描，找到最大的A_w
    w = N - 1
    for j in range(N - 2, -1, -1):
        if A[j] > A[w]:
            w = j
    # 从左到右扫描，找到最小的A_y
    y = x
    for i in range(x + 1, w + 1):
        if A[i] < A[y]:
            y = i
    # 从右到左扫描，找到最大的A_z
    z = w
    for j in range(w - 1, y - 1, -1):
        if A[j] > A[z]:
            z = j
    # 从左到右扫描，找到最小的A_y
    y = x
    for i in range(x + 1, z + 1):
        if A[i] < A[y]:
            y = i
    # 从右到左扫描，找到最大的A_z
    z = w
    for j in range(w - 1, y - 1, -1):
        if A[j] > A[z]:
            z = j
    # 从左到右扫描，找到最小的A_y
    y = x
    for i in range(x + 1, z + 1):
        if A[i] < A[y]:
            y = i
    # 从右到左扫描，找到最大的A_z
    z = w
    for j in range(w - 1, y - 1, -1):
        if A[j] > A[z]:
            z = j
    # 从左到右扫描，找到最小的A_y
    y = x
    for i in range

if __name__ == '__main__':
    main()