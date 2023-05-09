def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N-1):
        if S[i][0] != '!' and S[i] == S[i+1][1:]:
            print(S[i])
            return
    print("satisfiable")
