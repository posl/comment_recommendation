def main():
    S = input()
    K = int(input())
    N = len(S)
    X = 0
    Y = 0
    Z = 0
    if N == 1:
        print(1)
        return
    for i in range(N):
        if S[i] == 'X':
            X += 1
        else:
            Y += 1
            Z = max(Z, Y)
            if Y > K:
                Y = 0
    print(X + Z)

if __name__ == '__main__':
    main()