def main():
    N, A, B = map(int, input().split())
    if A + B == 0:
        print(0)
        return
    if A == 0:
        print(0)
        return
    if B == 0:
        print(N)
        return
    if A > B:
        A, B = B, A
    if N // (A + B) == 0:
        print(N // (A + B) * A + min(N % (A + B), A))
    else:
        print(N // (A + B) * A + min(N % (A + B), A))

if __name__ == '__main__':
    main()