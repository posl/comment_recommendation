def main():
    N, M = map(int, input().split())
    p = []
    S = []
    for i in range(M):
        p_i, S_i = input().split()
        p.append(int(p_i))
        S.append(S_i)
    # print(p)
    # print(S)
    # print(p[0])
    # print(S[0])
    # 正解数
    correct_number = 0
    # 罚分数
    penalty_number = 0
    # 按照问题的序号进行筛选
    for i in range(N):
        # 第i个问题的序号
        i = i + 1
        # print('i = ', i)
        # 按照问题的序号进行筛选
        for j in range(M):
            # print('j = ', j)
            # print('p[j] = ', p[j])
            # print('i = ', i)
            if p[j] == i:
                # print('p[j] = ', p[j])
                # print('i = ', i)
                # print('S[j] = ', S[j])
                if S[j] == 'AC':
                    correct_number = correct_number + 1
                    # print('correct_number = ', correct_number)
                    break
                elif S[j] == 'WA':
                    penalty_number = penalty_number + 1
                    # print('penalty_number = ', penalty_number)
    print(correct_number, penalty_number)
