def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    votes = sum(A)
    threshold = votes // (4 * M)
    if A[M - 1] >= threshold:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()