def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    P = 0
    for i in range(N):
        P += A[i] - 1
    print(P)

if __name__ == '__main__':
    main()