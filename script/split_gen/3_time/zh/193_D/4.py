def solve(K, S, T):
    # write code here
    S = S[:4]
    T = T[:4]
    S = [int(i) for i in S]
    T = [int(i) for i in T]
    S.sort()
    T.sort()
    S_back = int(S[3])
    T_back = int(T[3])
    S.pop()
    T.pop()
    S_sum = sum(S)
    T_sum = sum(T)
    S_sum += S_back * 10
    T_sum += T_back * 10
    if S_sum > T_sum:
        return 1
    elif S_sum == T_sum:
        return 0.5
    else:
        return 0
