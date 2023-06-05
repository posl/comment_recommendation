def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    S = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    S = input()
    #print("X=", X)
    #print("Y=", Y)
    #print("S=", S)
    flag = False
    for i in range(N-1):
        for j in range(i+1, N):
            if X[i] == X[j]:
                if S[i] == 'R' and S[j] == 'L':
                    flag = True
                    break
                elif S[i] == 'L' and S[j] == 'R':
                    flag = True
                    break
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()