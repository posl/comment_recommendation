def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N-1):
        if S[i] == S[i+1]:
            print(S[i])
            return
        if S[i] == "!" + S[i+1]:
            print(S[i+1])
            return
    print("satisfiable")
