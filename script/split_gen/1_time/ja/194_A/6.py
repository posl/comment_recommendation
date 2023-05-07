def main():
    #入力
    A, B = map(int, input().split())
    #処理
    if A + B >= 15 and B >= 8:
        ans = 1
    elif A + B >= 10 and B >= 3:
        ans = 2
    elif A + B >= 3:
        ans = 3
    else:
        ans = 4
    #出力
    print(ans)
