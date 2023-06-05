def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # 与城市i直接相连的城市数量（1 ≦ i ≦ N），这些城市为城市a_{i, 1}, ..., 城市a_{i, d_i}，依次递增

if __name__ == '__main__':
    main()