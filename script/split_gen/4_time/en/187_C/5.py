def main():
    N = int(input())
    S = [input() for i in range(N)]
    dic = {}
    for i in range(N):
        if S[i][0] == "!":
            if S[i][1:] in dic:
                print(S[i][1:])
                return
            else:
                dic[S[i][1:]] = 1
        else:
            if "!"+S[i] in dic:
                print(S[i])
                return
            else:
                dic[S[i]] = 1
    print("satisfiable")
    return
