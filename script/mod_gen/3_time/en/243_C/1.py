def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()
    if N == 2:
        if S[0] == S[1]:
            print("No")
        else:
            print("Yes")
        return
    for i in range(N):
        if S[i] == "R":
            X[i] = -X[i]
    X.sort()
    for i in range(N):
        if S[i] == "R":
            X[i] = -X[i]
    for i in range(N):
        if S[i] == "R":
            Y[i] = -Y[i]
    Y.sort()
    for i in range(N):
        if S[i] == "R":
            Y[i] = -Y[i]
    ans = "No"
    for i in range(N):
        if S[i] == "R":
            if X[i] < X[(i+1)%N]:
                ans = "Yes"
                break
        else:
            if X[i] > X[(i+1)%N]:
                ans = "Yes"
                break
    for i in range(N):
        if S[i] == "R":
            if Y[i] < Y[(i+1)%N]:
                ans = "Yes"
                break
        else:
            if Y[i] > Y[(i+1)%N]:
                ans = "Yes"
                break
    print(ans)

if __name__ == '__main__':
    main()