def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    i = 0
    j = 0
    while i < N:
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == M:
        print("Yes")
    else:
        print("No")
