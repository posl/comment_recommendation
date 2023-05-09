def main():
    N = int(input())
    S = [input() for _ in range(N)]
    D = {}
    for s in S:
        if s in D:
            D[s] += 1
            print(s + '(' + str(D[s]) + ')')
        else:
            D[s] = 0
            print(s)

if __name__ == '__main__':
    main()