def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S2 = []
    for i in range(N):
        if S[i][0] == '!':
            S2.append(S[i][1:])
        else:
            S2.append('!' + S[i])
    S2.sort()
    for i in range(N-1):
        if S2[i] == S2[i+1]:
            print(S2[i][1:])
            return
    print('satisfiable')
