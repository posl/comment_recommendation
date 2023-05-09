def main():
    #read input
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    #sort S
    S.sort(key=lambda s: [X.index(c) for c in s])
    #print output
    for s in S:
        print(s)

if __name__ == '__main__':
    main()