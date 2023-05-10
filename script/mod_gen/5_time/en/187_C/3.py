def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S_set = set(S)
    for s in S:
        if s[0] == '!':
            if s[1:] in S_set:
                print(s[1:])
                return
        else:
            if '!' + s in S_set:
                print(s)
                return
    print('satisfiable')

if __name__ == '__main__':
    main()