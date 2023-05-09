def main():
    N = int(input())
    S = [input() for i in range(N)]
    #print(N, S)
    if len(set(S)) != N:
        print('No')
        return
    for i in range(N):
        if S[i][0] not in 'HDCS':
            print('No')
            return
        if S[i][1] not in 'A23456789TJQK':
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()