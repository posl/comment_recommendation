def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    T = list(T)
    for i in range(N):
        if T[i] == 'r':
            T[i] = 'p'
        elif T[i] == 's':
            T[i] = 'r'
        else:
            T[i] = 's'
    T = "".join(T)
    T = T.replace('r','R')
    T = T.replace('s','S')
    T = T.replace('p','P')
    #print(T)
    ans = 0
    for i in range(N):
        if i < K:
            if T[i] == 'R':
                ans += R
            elif T[i] == 'S':
                ans += S
            else:
                ans += P
        else:
            if T[i] == 'R':
                if T[i-K] == 'R':
                    T = T[:i] + 'X' + T[i+1:]
                else:
                    ans += R
            elif T[i] == 'S':
                if T[i-K] == 'S':
                    T = T[:i] + 'X' + T[i+1:]
                else:
                    ans += S
            else:
                if T[i-K] == 'P':
                    T = T[:i] + 'X' + T[i+1:]
                else:
                    ans += P
    print(ans)

if __name__ == '__main__':
    main()