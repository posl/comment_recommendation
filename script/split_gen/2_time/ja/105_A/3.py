def main():
    #入力
    N,K = map(int,input().split())
    #処理
    if N%K == 0:
        print(0)
    else:
        print(1)
