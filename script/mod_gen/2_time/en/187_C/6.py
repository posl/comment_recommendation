def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = [s[1:] if s[0] == '!' else s for s in S]
    if len(S) != len(set(S)):
        print([s for s in S if S.count(s) > 1][0])
    else:
        print('satisfiable')

if __name__ == '__main__':
    main()