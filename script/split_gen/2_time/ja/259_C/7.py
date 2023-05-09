def main():
    S = input()
    T = input()
    N = len(T)
    M = len(S)
    #print(N,M)
    i = 0
    j = 0
    while i < N and j < M:
        if T[i] == S[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == M:
        print("Yes")
    else:
        print("No")
