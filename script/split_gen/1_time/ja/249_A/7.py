def main():
    # A B C D E F X
    a, b, c, d, e, f, x = map(int, input().split())
    # 1 ≦ A, B, C, D, E, F, X ≦ 100
    if 1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100 and 1 <= d <= 100 and 1 <= e <= 100 and 1 <= f <= 100 and 1 <= x <= 100:
        takahashi = 0
        aoki = 0
        for i in range(x):
            if i % (a + c) < a:
                takahashi += b
            if i % (d + f) < d:
                aoki += e
        # print(takahashi, aoki)
        if takahashi > aoki:
            print("Takahashi")
        elif takahashi < aoki:
            print("Aoki")
        else:
            print("Draw")
