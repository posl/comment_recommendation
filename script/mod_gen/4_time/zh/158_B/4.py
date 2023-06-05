def main():
    N, A, B = map(int, input().split())
    if N <= A + B:
        print(min(A, N))
    else:
        print(A + (N - A - B) * (A - B))

if __name__ == '__main__':
    main()