def solve():
    S = input()
    for i in range(len(S)):
        if i & 1 and S[i] in 'RL':
            print('No')
            return
        if not i & 1 and S[i] in 'UD':
            print('No')
            return
    print('Yes')
solve()
