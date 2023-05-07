def main():
    S = input()
    K = int(input())
    N = len(S)
    if N == 1:
        print(1)
        return
    if S[0] == '.':
        S = 'X' + S
        N += 1
    if S[-1] == '.':
        S = S + 'X'
        N += 1
    S = S.replace('.', 'X')
    #print(S)
    max = 0
    cnt = 0
    for i in range(1, N):
        if S[i] == 'X':
            cnt += 1
        else:
            if cnt > max:
                max = cnt
            cnt = 0
    if cnt > max:
        max = cnt
    #print(max)
    if max > K:
        max = K
    print(max + 1)
