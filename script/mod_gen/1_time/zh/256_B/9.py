def main():
    # N = 4
    # A = [1,1,3,2]
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += A[i] - 1
    print(P)

if __name__ == '__main__':
    main()