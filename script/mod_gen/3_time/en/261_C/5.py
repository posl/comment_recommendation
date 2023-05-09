def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = []
    for s in S:
        if s not in T:
            T.append(s)
            print(s)
        else:
            print(s + '(' + str(T.count(s)) + ')')
            T.append(s)

if __name__ == '__main__':
    main()