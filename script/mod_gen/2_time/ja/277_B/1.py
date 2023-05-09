def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if len(set(S)) == N and all(s[0] in 'HDCS' and s[1] in 'A23456789TJQK' for s in S):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()