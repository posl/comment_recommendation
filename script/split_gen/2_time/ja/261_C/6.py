def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = set()
    for i in range(N):
        if S[i] in T:
            print(S[i] + "(" + str(S[:i].count(S[i])) + ")")
        else:
            print(S[i])
        T.add(S[i])
main()
