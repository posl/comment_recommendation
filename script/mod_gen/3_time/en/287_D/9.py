def solve():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S_ = S[:i] + S[-(len(T)-i):]
        if all([s==t or s=='?' or t=='?' for s,t in zip(S_,T)]):
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    solve()