def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N % 2 == 0:
        print(sum(A))
    else:
        print(sum(A) - 2 * min(abs(i) for i in A))

if __name__ == '__main__':
    main()