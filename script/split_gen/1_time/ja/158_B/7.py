def main():
    #入力
    N, A, B = map(int, input().split())
    #処理
    if A == 0:
        print(0)
    elif A + B <= N:
        print(A * (N // (A + B)) + min(A, N % (A + B)))
    else:
        print(min(A, N))
