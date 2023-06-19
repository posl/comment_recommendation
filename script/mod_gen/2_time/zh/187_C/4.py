def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S = set(S)
    for s in S:
        if s[0] == '!':
            if s[1:] in S:
                return print(s[1:])
        else:
            if '!'+s in S:
                return print(s)
    print('satisfiable')

if __name__ == '__main__':
    main()