def main():
    #入力
    a, b, c = map(int, input().split())
    #中央値の判定
    if (a <= b <= c) or (c <= b <= a):
        print("Yes")
    else:
        print("No")
