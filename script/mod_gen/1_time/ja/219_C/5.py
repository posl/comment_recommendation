def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    T = [sorted(s, key=lambda x: X.index(x)) for s in S]
    for s, t in sorted(zip(S, T), key=lambda x: x[1]):
        print(s)

if __name__ == '__main__':
    main()