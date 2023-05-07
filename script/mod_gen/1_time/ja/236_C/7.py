def main():
    #N, M = map(int, input().split())
    #S = list(map(str, input().split()))
    #T = list(map(str, input().split()))
    N, M = 5, 3
    S = ['tokyo', 'kanda', 'akiba', 'okachi', 'ueno']
    T = ['tokyo', 'akiba', 'ueno']
    for i in range(N):
        if S[i] in T:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()