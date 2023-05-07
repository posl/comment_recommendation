def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    d = {}
    for s in S:
        if s not in d:
            d[s] = 0
            print(s)
        else:
            d[s] += 1
            print(s + "(" + str(d[s]) + ")")
main()

if __name__ == '__main__':
    main()