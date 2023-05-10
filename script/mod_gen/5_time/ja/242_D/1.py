def main():
    S = input()
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    for t, k in query:
        t %= 3
        if t == 0:
            print(S[k-1])
        elif t == 1:
            print(S[k-1].translate(str.maketrans('ABC', 'BCA')))
        else:
            print(S[k-1].translate(str.maketrans('ABC', 'CAB')))

if __name__ == '__main__':
    main()