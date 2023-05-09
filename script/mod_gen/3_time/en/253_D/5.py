def main():
    N, A, B = map(int, input().split())
    if A > B:
        A, B = B, A
    if A == B:
        print(N // A)
    else:
        print((N // A) * (N // B) * (A + B) // 2)

if __name__ == '__main__':
    main()