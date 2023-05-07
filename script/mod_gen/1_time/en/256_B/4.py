def main():
    N = int(input())
    A = list(map(int,input().split()))
    P = 0
    for i in range(N):
        P = P + A[i]//4
        A[i] = A[i]%4
    if sum(A) >= 4:
        P = P + 1
    print(P)

if __name__ == '__main__':
    main()