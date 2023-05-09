def main():
    # 入力
    n,k = map(int,input().split())
    # 処理
    for i in range(k):
        if n%200==0:
            n=n//200
        else:
            n=int(str(n)+"200")
    # 出力
    print(n)
