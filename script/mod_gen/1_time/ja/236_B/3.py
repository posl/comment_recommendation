def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0 for i in range(N+1)]
    for i in range(4*N-1):
        B[A[i]] += 1
    for i in range(1,N+1):
        if B[i] % 2 == 1:
            print(i)
            break

if __name__ == '__main__':
    main()