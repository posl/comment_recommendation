def main():
    # 1行目の入力
    a = list(map(int,input().split()))
    # 0が表示されている状態からボタンを3回押すと、画面には何が表示されるか
    print(a[a[a[0]]])
