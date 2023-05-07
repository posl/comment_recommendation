def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print('Yes' if len(S) == len(set(S)) and all(s[0] in 'HDCS' and s[1] in 'A23456789TJQK' for s in S) else 'No')

if __name__ == '__main__':
    main()