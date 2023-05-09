def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = list(input())
    for i in range(N):
        if S[i] == "R":
            for j in range(N):
                if i == j:
                    continue
                if S[j] == "L":
                    if X[i] == X[j] and Y[i] < Y[j]:
                        print("Yes")
                        return
        else:
            for j in range(N):
                if i == j:
                    continue
                if S[j] == "R":
                    if X[i] == X[j] and Y[i] > Y[j]:
                        print("Yes")
                        return
    print("No")
    return

if __name__ == '__main__':
    main()