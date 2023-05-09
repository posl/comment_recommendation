def main():
    N = int(input())
    S = [input() for i in range(N)]
    D = {}
    for s in S:
        if s in D:
            D[s] += 1
        else:
            D[s] = 1
        if D[s] == 1:
            print(s)
        else:
            print(s + '(' + str(D[s]) + ')')

if __name__ == '__main__':
    main()