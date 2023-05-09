def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    if S[0][0] not in ['H','D','C','S'] or S[0][1] not in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']:
        print('No')
        return
    for i in range(1,N):
        if S[i][0] not in ['H','D','C','S'] or S[i][1] not in ['A','2','3','4','5','6','7','8','9','T','J','Q','K'] or S[i-1] == S[i]:
            print('No')
            return
    print('Yes')
