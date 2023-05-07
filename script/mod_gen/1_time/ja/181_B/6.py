def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    print(sum((B[i]-A[i]+1)*(A[i]+B[i])//2 for i in range(N))%(10**9+7))

if __name__ == '__main__':
    main()