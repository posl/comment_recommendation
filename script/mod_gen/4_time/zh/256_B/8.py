def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if A[i] + i < 4:
            P += 0
        else:
            P += A[i] + i - 3
    print(P)

if __name__ == '__main__':
    main()