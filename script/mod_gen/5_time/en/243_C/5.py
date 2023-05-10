def main():
    N = int(input())
    XY = []
    for i in range(N):
        XY.append(list(map(int,input().split())))
    S = input()
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i] = XY[i][0]
        Y[i] = XY[i][1]
    for i in range(N):
        if S[i] == "R":
            X[i] += 1
        elif S[i] == "L":
            X[i] -= 1
    for i in range(N):
        for j in range(N):
            if i != j:
                if X[i] == X[j] and Y[i] == Y[j]:
                    print("Yes")
                    exit()
    print("No")

if __name__ == '__main__':
    main()