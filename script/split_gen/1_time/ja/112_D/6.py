def main():
    N, M = map(int, input().split())
    #MをNで割ったあまりを求める
    mod = M % N
    #MをNで割った商を求める
    div = M // N
    #MをNで割ったあまりが0の場合は、MをNで割った商が答えとなる
    if mod == 0:
        print(div)
    #MをNで割ったあまりが0でない場合は、MをNで割った商の数だけMをNで割ったあまりを1ずつ足す
    else:
        print(div + 1)
