def main():
    #入力
    R, C = map(int, input().split())
    #出力
    if (R + C) % 2 == 0:
        print("black")
    else:
        print("white")
