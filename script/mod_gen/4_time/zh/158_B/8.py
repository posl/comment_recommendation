def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif B == 0:
        print(N)
    else:
        print(N // (A + B) * A + min(N % (A + B), A))

if __name__ == '__main__':
    main()