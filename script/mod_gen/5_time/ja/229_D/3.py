def main():
    S = input()
    K = int(input())
    S = S.replace(".","X")
    X = 0
    for i in range(len(S)-1):
        if S[i] == "X":
            if S[i+1] == "X":
                X += 1
    if K == 0:
        print(X)
    else:
        if S[0] == "X":
            if S[-1] == "X":
                print(X+K*2)
            else:
                print(X+K)
        else:
            if S[-1] == "X":
                print(X+K)
            else:
                print(X+K-1)

if __name__ == '__main__':
    main()