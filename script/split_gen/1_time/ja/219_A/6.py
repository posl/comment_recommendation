def main():
    # 0 ≦ X ≦ 100
    # X は整数
    X = int(input())
    if X == 100:
        print("expert")
    elif X >= 90:
        print(100 - X)
    elif X >= 70:
        print(90 - X)
    elif X >= 40:
        print(70 - X)
    else:
        print(40 - X)
