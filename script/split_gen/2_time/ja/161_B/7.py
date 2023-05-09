def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #総投票数
    total = sum(A)
    #人気商品の得票数
    A.sort(reverse=True)
    popular = A[:M]
    #人気商品の得票数が総投票数の (1/(4M)) 未満であるか
    if min(popular) < total//(4*M):
        print("No")
    else:
        print("Yes")
