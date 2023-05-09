def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "U":
            X = (X + 1) // 2
        elif S[i] == "L":
            X *= 2
        elif S[i] == "R":
            X = X * 2 + 1
        else:
            print("error")
    print(X)

if __name__ == '__main__':
    main()