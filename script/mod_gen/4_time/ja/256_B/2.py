def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += A[i] - 1
    print(P)
main()

if __name__ == '__main__':
    main()