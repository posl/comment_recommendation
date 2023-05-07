def main():
    N = int(input())
    B = list(map(int,input().split()))
    B.append(0)
    A = [0] * N
    for i in range(N-1):
        A[i] = min(B[i], B[i+1])
    print(sum(A))

if __name__ == '__main__':
    main()