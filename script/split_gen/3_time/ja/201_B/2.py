def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))
    T_max = max(T)
    T.remove(T_max)
    T_second = max(T)
    print(S[T.index(T_second)])
