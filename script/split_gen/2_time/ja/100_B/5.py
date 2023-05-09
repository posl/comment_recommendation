def main():
    #入力
    D, N = map(int, input().split())
    #処理
    if D == 0:
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(10100)
        else:
            print(100 * N)
    else:
        if N == 100:
            print(1010000)
        else:
            print(10000 * N)
