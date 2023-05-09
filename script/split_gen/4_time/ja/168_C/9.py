def main():
    import math
    A, B, H, M = map(int, input().split())
    angle = 0
    #角度は時針と分針の角度の差
    angle = abs((H * 60 + M) * 0.5 - M * 6)
    #角度をラジアンに変換
    rad = angle * math.pi / 180
    #余弦定理
    ans = A ** 2 + B ** 2 - 2 * A * B * math.cos(rad)
    print(math.sqrt(ans))
