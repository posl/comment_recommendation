def main():
    # 標準入力の受け取り
    N,K = map(int,input().split())
    S = input()
    # 0の連続個数をカウント
    zero = 0
    zero_list = []
    for i in range(N):
        if S[i] == '0':
            zero += 1
        else:
            zero_list.append(zero)
            zero = 0
    zero_list.append(zero)
    # 0の連続個数のリストから、K回の指示で反転できる最大値を求める
    if len(zero_list) <= K:
        print(N)
    else:
        max_zero = 0
        for i in range(len(zero_list)-K):
            zero_sum = sum(zero_list[i:i+K+1])
            if zero_sum > max_zero:
                max_zero = zero_sum
        print(max_zero)
