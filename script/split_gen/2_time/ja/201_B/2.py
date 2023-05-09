def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    T_max = max(T)
    T[T.index(T_max)] = 0
    T_2nd = max(T)
    print(S[T.index(T_2nd)])
