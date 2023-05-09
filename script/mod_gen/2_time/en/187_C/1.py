def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        if "!" + S[i] in S:
            print(S[i])
            return
    print("satisfiable")
    return

if __name__ == '__main__':
    main()