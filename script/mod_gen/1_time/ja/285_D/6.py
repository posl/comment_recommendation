def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    print('Yes' if solve(N, S, T) else 'No')

if __name__ == '__main__':
    main()