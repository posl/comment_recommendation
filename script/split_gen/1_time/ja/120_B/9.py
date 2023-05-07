def main():
    # 入力
    A, B, K = map(int, input().split())
    # リストを作成
    list = []
    # A,Bの最大公約数を求める
    for i in range(1, min(A, B)+1):
        if A % i == 0 and B % i == 0:
            list.append(i)
    # 出力
    print(list[-K])
