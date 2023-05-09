def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input().split())
        T.append(int(S[i][1]))
    T.sort()
    for i in range(N):
        if T[-2] == int(S[i][1]):
            print(S[i][0])
            break
