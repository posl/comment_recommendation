def main():
    N = int(input())
    S = [input() for i in range(N)]
    for i in range(N):
        if S[i][0] == "!":
            if S[i][1:] in S:
                print(S[i][1:])
                return
        else:
            if "!" + S[i] in S:
                print(S[i])
                return
    print("satisfiable")
    return
