def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[0:N-2]))
main()

if __name__ == '__main__':
    main()