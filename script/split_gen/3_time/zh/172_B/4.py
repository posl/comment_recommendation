def solve():
    # 解题算法
    S = input()
    T = input()
    if S == T:
        return 0
    ans = 10**5
    for i in range(len(S)-len(T)+1):
        count = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                count += 1
        ans = min(ans, count)
    return ans
