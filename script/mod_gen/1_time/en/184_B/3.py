def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "x":
            if X > 0:
                X -= 1
        else:
            X += 1
    print(X)

if __name__ == '__main__':
    main()