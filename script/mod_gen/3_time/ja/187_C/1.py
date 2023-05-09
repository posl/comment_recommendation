def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N-1):
        if S[i][0] == "!":
            if S[i][1:] == S[i+1]:
                print(S[i][1:])
                return
    print("satisfiable")
    return

if __name__ == '__main__':
    main()