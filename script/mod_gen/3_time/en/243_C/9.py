def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        X.append(int(input()))
        Y.append(int(input()))
    S = input()
    for i in range(N):
        if S[i] == "R":
            for j in range(i+1,N):
                if S[j] == "L":
                    if Y[i] == Y[j]:
                        print("Yes")
                        return
        else:
            for j in range(i+1,N):
                if S[j] == "R":
                    if Y[i] == Y[j]:
                        print("Yes")
                        return
    print("No")
    return

if __name__ == '__main__':
    main()