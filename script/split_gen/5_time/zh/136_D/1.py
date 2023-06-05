def main():
    # 读入数据
    S = input()
    # 处理数据
    N = len(S)
    # 从左向右计算
    R = [0] * N
    for i in range(N):
        if S[i] == 'R':
            if i == 0:
                R[i] = 1
            else:
                R[i] = R[i-1] + 1
        else:
            R[i] = 0
    # 从右向左计算
    L = [0] * N
    for i in range(N-1, -1, -1):
        if S[i] == 'L':
            if i == N-1:
                L[i] = 1
            else:
                L[i] = L[i+1] + 1
        else:
            L[i] = 0
    # 计算结果
    result = [0] * N
    for i in range(N):
        if S[i] == 'R':
            if i+L[i] < N:
                result[i+L[i]] += 1
            else:
                result[N-1] += 1
        else:
            if i-R[i] >= 0:
                result[i-R[i]] += 1
            else:
                result[0] += 1
    # 输出结果
    print(" ".join(map(str, result)))
