def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    # 1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15, ...
    # 1, 2, 4, 8, 16, 17, 18, 19, 20, 21, 22, ...
    # 1, 2, 4, 8, 16, 32, 33, 34, 35, 36, 37, ...
    # 1, 2, 4, 8, 16, 32, 64, 65, 66, 67, 68, ...
    # 1, 2, 4, 8, 16, 32, 64, 128, 129, 130, 131, ...
    # 1, 2, 4, 8, 16, 32, 64, 128, 256, 257, 258, ...
    # 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 513, ...
    # 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, ...
    # 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, ...
    # 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, ...
    # 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, ...
    # 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 204
