def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    T_max = max(T)
    T.remove(T_max)
    T_max = max(T)
    print(S[T.index(T_max)])

if __name__ == '__main__':
    main()