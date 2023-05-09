def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    # 1つ目の最大値を求める
    max1 = 0
    for i in range(N):
        if A[i] > max1:
            max1 = A[i]
            max1_index = i
    # 2つ目の最大値を求める
    max2 = 0
    for i in range(N):
        if i == max1_index:
            continue
        if A[i] > max2:
            max2 = A[i]
    # 出力
    for i in range(N):
        if i == max1_index:
            print(max2)
        else:
            print(max1)
