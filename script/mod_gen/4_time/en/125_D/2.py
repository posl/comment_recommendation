def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] < 0:
        if N % 2 == 0:
            print(sum(map(abs, A)))
        else:
            print(sum(map(abs, A)) - 2 * min(map(abs, A)))
    else:
        print(sum(A))

if __name__ == '__main__':
    main()