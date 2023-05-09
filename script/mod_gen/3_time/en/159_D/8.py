def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    #count
    B = [0]*(N+1)
    for i in A:
        B[i] += 1
    #output
    for i in range(N):
        print(B[A[i]]-1)

if __name__ == '__main__':
    main()