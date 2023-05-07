def main():
    N = int(input())
    P = list(map(int, input().split()))
    # 人iの親を親リストに格納
    parent_list = [0] * N
    for i in range(1, N):
        parent_list[i] = P[i-1]
    # 人iの親の親を親リストに格納
    for i in range(1, N):
        parent_list[i] = parent_list[parent_list[i]-1]
    # 親リストの最大値を出力
    print(max(parent_list))
