def main():
    S = input()
    N = len(S)
    L = [0] * N
    R = [0] * N
    L[0] = 1
    R[-1] = 1
    for i in range(1, N):
        if S[i-1] == "L":
            L[i] = L[i-1] + 1
        else:
            L[i] = L[i-1]
    for i in range(N-2, -1, -1):
        if S[i] == "R":
            R[i] = R[i+1] + 1
        else:
            R[i] = R[i+1]
    for i in range(N):
        print((L[i] + R[i]) // 2, end=" ")
    print()
