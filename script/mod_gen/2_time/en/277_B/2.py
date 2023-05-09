def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if len(set(S)) != len(S):
        print('No')
        return
    for s in S:
        if s[0] not in 'HDCS' or s[1] not in 'A23456789TJQK':
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()