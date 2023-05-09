def main():
    #入力
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    #昇順に並べ替える
    B = sorted(A)
    #連続してK個の数が同じ数値になっているかを確認する
    flag = True
    for i in range(N-K):
        if B[i] != B[i+K]:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")
