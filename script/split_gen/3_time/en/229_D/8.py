def main():
    S = input()
    K = int(input())
    N = len(S)
    S = S.replace('.','X')
    if K == 0:
        print(S)
        return
    if S[0] == 'X':
        C = 1
        for i in range(1,N):
            if S[i] == 'X':
                C += 1
            else:
                break
        if C >= K:
            print(C)
            return
        else:
            K -= C
    if S[-1] == 'X':
        C = 1
        for i in range(N-2,-1,-1):
            if S[i] == 'X':
                C += 1
            else:
                break
        if C >= K:
            print(C)
            return
        else:
            K -= C
    C = 0
    for i in range(1,N-1):
        if S[i] == 'X':
            C += 1
        else:
            C = 0
        if C >= K:
            print(C)
            return
    print('0')
