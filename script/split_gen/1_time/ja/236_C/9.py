def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    i = 0
    j = 0
    for i in range(N):
        if S[i] == T[j]:
            print("Yes")
            j += 1
        else:
            print("No")
        if j == M:
            break
    for i in range(i + 1, N):
        print("No")
