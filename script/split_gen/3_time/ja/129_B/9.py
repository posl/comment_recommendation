def main():
    N = int(input())
    W = list(map(int,input().split()))
    # 全ての重りを左から右に移動させて、左側の重りの重さの和を計算していく
    # その際に最小値を更新していく
    sum = 0
    min = 100000
    for i in range(N):
        sum += W[i]
        if i < N-1:
            if abs(sum - (sum - W[i])) < min:
                min = abs(sum - (sum - W[i]))
    print(min)
