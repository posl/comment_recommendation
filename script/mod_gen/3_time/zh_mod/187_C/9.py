def main():
    N = int(input())
    S = [input() for i in range(N)]
    S1 = set()
    S2 = set()
    for s in S:
        if s[0] == '!':
            S1.add(s[1:])
        else:

if __name__ == '__main__':
    main()