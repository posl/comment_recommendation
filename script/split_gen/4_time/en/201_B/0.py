def main():
    N = int(input())
    S = [0] * N
    T = [0] * N
    for i in range(N):
        S[i], T[i] = input().split()
        T[i] = int(T[i])
    T_max = max(T)
    T[T.index(T_max)] = 0
    print(S[T.index(max(T))])
