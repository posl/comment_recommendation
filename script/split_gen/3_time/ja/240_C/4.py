def main():
    #入力
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #処理
    for i in range(N):
        if X <= a[i]:
            X = X - a[i]
        else:
            X = X - b[i]
    #出力
    if X == 0:
        print("Yes")
    else:
        print("No")
