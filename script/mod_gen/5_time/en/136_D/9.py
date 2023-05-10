def main():
    S = input()
    N = len(S)
    A = [0] * N
    #print(S)
    #print(N)
    #print(A)
    #print(S[0])
    #print(S[1])
    #print(S[0] == "R")
    #print(S[1] == "R")
    #print(S[0] == "L")
    #print(S[1] == "L")
    #print(S[0] == "R" and S[1] == "R")
    #print(S[0] == "R" and S[1] == "L")
    #print(S[0] == "L" and S[1] == "R")
    #print(S[0] == "L" and S[1] == "L")
    if S[0] == "R" and S[1] == "R":
        A[0] += 1
    if S[0] == "R" and S[1] == "L":
        A[0] += 1
        A[1] += 1
    if S[0] == "L" and S[1] == "R":
        A[0] += 1
        A[1] += 1
    if S[0] == "L" and S[1] == "L":
        A[1] += 1
    #print(A)
    for i in range(1, N - 1):
        if S[i] == "R" and S[i + 1] == "R":
            A[i] += 1
        if S[i] == "R" and S[i + 1] == "L":
            A[i] += 1
            A[i + 1] += 1
        if S[i] == "L" and S[i + 1] == "R":
            A[i] += 1
            A[i + 1] += 1
        if S[i] == "L" and S[i + 1] == "L":
            A[i + 1] += 1
    #print(A)
    if S[N - 2] == "R" and S[N - 1] == "R":
        A[N - 2] += 1

if __name__ == '__main__':
    main()