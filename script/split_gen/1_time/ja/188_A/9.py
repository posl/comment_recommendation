def main():
    #入力
    X, Y = map(int, input().split())
    #処理
    if X < Y:
        if (Y - X) < 3:
            print("Yes")
        else:
            print("No")
    else:
        if (X - Y) < 3:
            print("Yes")
        else:
            print("No")
