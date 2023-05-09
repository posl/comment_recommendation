def main():
    # Take input
    N, X = map(int, input().split())
    S = input()
    # Solve problem
    for i in range(N):
        if S[i] == 'o':
            X += 1
        else:
            if X > 0:
                X -= 1
    # Output result
    print(X)

if __name__ == '__main__':
    main()