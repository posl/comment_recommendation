def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    #print(n)
    #print(a)
    #print(2**n)
    #print("n:", n)
    #print("a:", a)
    #print("2**n:", 2**n)
    # まずは、2^nのリストを作成
    # 1, 2, 4, 8, 16, 32, 64, 128, 256, 512
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
    # 0, 4, 8, 12, 16, 20, 24, 28, 32, 36
    # 0, 8, 16, 24, 32, 40, 48, 56, 64, 72
    # 0, 16, 32, 48, 64, 80, 96, 112, 128, 144
    # 0, 32, 64, 96, 128, 160, 192, 224, 256, 288
    # 0, 64, 128, 192, 256, 320, 384, 448, 512, 576
    # 0, 128, 256, 384, 512, 640, 768, 896, 1024, 1152
    # 0, 256, 512, 768, 1024, 1280, 1536, 1792, 2048, 2304
    # 0, 512, 1024, 1536, 2048, 2560, 3072, 3584, 4096, 4608
    # 0, 1024, 2048, 3072, 4096, 5120, 6144, 7168, 8192, 9216
    # 0,
