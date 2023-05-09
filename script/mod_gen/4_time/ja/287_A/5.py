def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        if S[i] == 'For':
            S[i] = 1
        else:
            S[i] = 0
    if sum(S) > N/2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()