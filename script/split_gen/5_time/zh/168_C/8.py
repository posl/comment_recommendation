def main():
    A, B, H, M = map(int, input().split())
    import math
    # 角度をラジアンに変換
    H_rad = (H * 60 + M) / 720 * math.pi * 2
    M_rad = M / 60 * math.pi * 2
    # 余弦定理
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(H_rad - M_rad)))
