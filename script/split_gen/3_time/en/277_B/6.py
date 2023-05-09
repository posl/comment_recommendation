def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    if len(set(S)) == N:
        for i in range(N):
            if S[i][0] not in ['H', 'D', 'C', 'S']:
                print('No')
                break
            elif S[i][1] not in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
                print('No')
                break
        else:
            print('Yes')
    else:
        print('No')
