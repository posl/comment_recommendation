def main():
    N, L = map(int, input().split())
    if L >= 0:
        print((N-1)*L + N*(N-1)//2)
    elif L + N - 1 < 0:
        print((N-1)*L + N*(N-1)//2 - L - N + 1)
    else:
        print((N-1)*L + N*(N-1)//2)

if __name__ == '__main__':
    main()