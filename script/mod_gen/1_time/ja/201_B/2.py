def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    max1 = max(T)
    T.remove(max1)
    max2 = max(T)
    print(S[T.index(max2)])

if __name__ == '__main__':
    main()