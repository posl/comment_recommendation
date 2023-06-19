def main():
    L = int(input())
    N = 0
    M = 0
    # 1. 从L开始，逐渐减小，直到找到一个L，使得N*M<=60
    while True:
        N = L
        while N >= 2:
            M = L // N
            if M * N == L:
                break
            N -= 1
        if M * N == L:
            break
        L -= 1
    print(N, M)
    # 2. 构建图
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, M-1):
        print(i, i+1, i)
    print(1, M, L)
