def main():
    A, B, K = map(int, input().split())
    if A >= K:
        A -= K
    elif A < K:
        K -= A
        A = 0
        if B >= K:
            B -= K
        elif B < K:
            B = 0
    print(A, B)

if __name__ == '__main__':
    main()