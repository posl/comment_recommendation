def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    # 最大値の個数
    max_num = 0
    # 最大値
    max_val = 0
    # 2番目に大きい値
    second_max_val = 0
    for i in range(N):
        if max_val < A[i]:
            max_val = A[i]
            max_num = 1
        elif max_val == A[i]:
            max_num += 1
        elif second_max_val < A[i]:
            second_max_val = A[i]
    for i in range(N):
        if A[i] == max_val and max_num == 1:
            print(second_max_val)
        else:
            print(max_val)
