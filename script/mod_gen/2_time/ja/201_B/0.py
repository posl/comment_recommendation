def main():
    N = int(input())
    S = [0] * N
    T = [0] * N
    for i in range(N):
        S[i], T[i] = input().split()
        T[i] = int(T[i])
    T2 = sorted(T)
    print(S[T.index(T2[-2])])

if __name__ == '__main__':
    main()