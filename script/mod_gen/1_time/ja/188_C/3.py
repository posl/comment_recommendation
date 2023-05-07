def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(2**(N-i)):
            if A[2*j] > A[2*j+1]:
                A[2*j] = 0
            else:
                A[2*j+1] = 0
    for i in range(2**N):
        if A[i] != 0:
            ans = i+1
    print(ans)

if __name__ == '__main__':
    main()