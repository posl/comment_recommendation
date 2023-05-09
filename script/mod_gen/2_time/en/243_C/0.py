def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'R':
            for j in range(i+1, N):
                if S[j] == 'L':
                    if X[i] < X[j] and Y[i] == Y[j]:
                        print("Yes")
                        return
        else:
            for j in range(i+1, N):
                if S[j] == 'R':
                    if X[i] > X[j] and Y[i] == Y[j]:
                        print("Yes")
                        return
    print("No")

if __name__ == '__main__':
    main()