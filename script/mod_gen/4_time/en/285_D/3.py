def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        if S[i] in T:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()