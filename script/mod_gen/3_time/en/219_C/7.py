def main():
    # read data
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    # sort data
    sorted_S = sorted(S, key=lambda x: [X.index(c) for c in x])
    # output
    for s in sorted_S:
        print(s)

if __name__ == '__main__':
    main()