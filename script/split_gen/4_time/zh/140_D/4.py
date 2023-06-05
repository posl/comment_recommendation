def main():
    N,K = map(int,input().split())
    S = input()
    S = S.replace('LR','R')
    S = S.replace('RL','L')
    if S[0] == 'R':
        S = 'L' + S
    if S[-1] == 'L':
        S = S + 'R'
    #print(S)
    count = 0
    for i in range(N-1):
        if S[i] == 'R' and S[i+1] == 'L':
            count += 1
    #print(count)
    if count <= K:
        print(N-1)
    else:
        print(N-1-(count-K)*2)
