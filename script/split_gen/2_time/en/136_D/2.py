def main():
    S = input()
    N = len(S)
    L = [0] * N
    R = [0] * N
    for i in range(N):
        if S[i] == "R":
            R[i] = 1
        else:
            L[i] = 1
    for i in range(N):
        if i > 0:
            L[i] += L[i - 1]
    for i in range(N - 1, -1, -1):
        if i < N - 1:
            R[i] += R[i + 1]
    ans = []
    for i in range(N):
        if S[i] == "R":
            ans.append(L[i] + R[i + 1] - 1)
        else:
            ans.append(L[i - 1] + R[i] - 1)
    print(" ".join(map(str, ans)))
