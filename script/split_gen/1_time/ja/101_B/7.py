def main():
    #入力
    N = int(input())
    #S(N)を計算
    S = 0
    while N > 0:
        S += N % 10
        N //= 10
    #S(N)で割り切れるか判定
    if N % S == 0:
        print('Yes')
    else:
        print('No')
