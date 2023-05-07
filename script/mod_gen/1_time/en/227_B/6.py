def main():
    N = int(input())
    S = list(map(int, input().split()))
    if (4 * min(S) + 3 * S.index(min(S)) + 3 * (N - S.index(min(S)) - 1)) <= max(S):
        print(0)
    else:
        print(N - 1)

if __name__ == '__main__':
    main()