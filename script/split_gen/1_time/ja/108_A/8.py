def main():
    # 入力
    k = int(input())
    # 処理
    if k%2==0:
        k = k//2
        print(k*(k-1))
    else:
        k = k//2
        print(k*(k+1))
