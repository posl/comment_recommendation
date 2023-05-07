def main():
    N = int(input())
    S = [input() for i in range(N)]
    D = {}
    for s in S:
        if s not in D:
            D[s] = 1
            print(s)
        else:
            print(s + '(' + str(D[s]) + ')')
            D[s] += 1
    return

if __name__ == '__main__':
    main()