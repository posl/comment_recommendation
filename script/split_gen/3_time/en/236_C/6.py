def main():
    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())
    S_set = set(S)
    T_set = set(T)
    S_T = S_set & T_set
    for i in range(N):
        if S[i] in S_T:
            print('Yes')
        else:
            print('No')
