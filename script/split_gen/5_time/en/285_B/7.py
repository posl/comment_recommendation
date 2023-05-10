def main():
    S = input()
    N = len(S)
    L = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            if S[i] != S[j]:
                L[i] = max(L[i], j-i)
            else:
                break
    for i in range(N-1):
        print(L[i])
