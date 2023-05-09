def main():
    N = int(input())
    S = [input() for _ in range(N)]
    s = set()
    for i in range(N):
        if S[i][0] == "!":
            if S[i][1:] in s:
                print(S[i][1:])
                return
        else:
            if "!" + S[i] in s:
                print(S[i])
                return
        s.add(S[i])
    print("satisfiable")

if __name__ == '__main__':
    main()