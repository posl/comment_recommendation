def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2**N)
    for i in range(2**N):
        B[i] = [A[i],i+1]
    for i in range(N):
        for j in range(2**(N-i-1)):
            if B[2*j][0] > B[2*j+1][0]:
                B[j] = B[2*j]
            else:
                B[j] = B[2*j+1]
    print(B[0][1])

if __name__ == '__main__':
    main()