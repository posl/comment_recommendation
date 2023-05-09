def main():
    X = int(input())
    # 500円硬貨の枚数
    n = X // 500
    # 5円硬貨の枚数
    m = (X - n * 500) // 5
    print(n * 1000 + m * 5)
