def main():
    N = int(input())
    S = [None] * N
    T = [None] * N
    for i in range(N):
        S[i], T[i] = input().split()
        T[i] = int(T[i])
    print(N - max(T) + 1)
