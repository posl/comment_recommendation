def main():
    S = input()
    Q = S.count('?')
    # 1. 确定S中的C的位置
    cs = []
    for i in range(len(S)):
        if S[i] == 'C':
            cs.append(i)
    # 2. 确定S中的B的位置
    bs = []
    for c in cs:
        bs.append(S[:c].count('B'))
    # 3. 确定S中的A的位置
    ans = 0
    for b in bs:
        ans += S[:b].count('A')
    # 4. 计算答案
    for c in cs:
        ans += S[c:].count('A') * S[c:].count('B')
    # 5. 计算答案
    for q in range(Q):
        ans *= 3
    # 6. 打印答案
    print(ans % (10**9 + 7))
