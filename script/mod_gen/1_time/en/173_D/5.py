def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(max(A))
        return
    A.sort()
    print(A[-1] + sum(A[:-1]))

if __name__ == '__main__':
    main()