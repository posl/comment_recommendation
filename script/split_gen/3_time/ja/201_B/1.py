def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S_i, T_i = input().split()
        S.append(S_i)
        T.append(int(T_i))
    T_max = max(T)
    T_max_index = T.index(T_max)
    T[T_max_index] = 0
    T_second_max = max(T)
    T_second_max_index = T.index(T_second_max)
    print(S[T_second_max_index])
