def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # A と B の各要素を値とする辞書を作成
    dict_A = {A[i]: i for i in range(N)}
    dict_B = {B[i]: i for i in range(N)}
    # 1. A にも B にも含まれ、その位置も一致している整数の個数
    count = 0
    for i in range(N):
        if dict_A[B[i]] == i:
            count += 1
    print(count)
    # 2. A にも B にも含まれるが、その位置は異なる整数の個数
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if dict_A[B[i]] == j and dict_B[A[i]] == j:
                count += 1
    print(count)
