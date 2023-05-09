def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(2*N):
        if A[i] != A[i+2*N]:
            print(A[i])
            break

if __name__ == '__main__':
    main()