def main():
    N = int(input())
    S = [input() for _ in range(N)]
    d = {}
    for s in S:
        if s not in d:
            d[s] = 1
            print(s)
        else:
            print(s + '(' + str(d[s]) + ')')
            d[s] += 1

if __name__ == '__main__':
    main()