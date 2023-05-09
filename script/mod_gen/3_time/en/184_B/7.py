def main():
    # Read the input
    N, X = map(int, input().split())
    S = input()
    # Solve the problem
    for i in range(N):
        if S[i] == 'o':
            X += 1
        elif S[i] == 'x' and X > 0:
            X -= 1
    # Print the answer
    print(X)

if __name__ == '__main__':
    main()