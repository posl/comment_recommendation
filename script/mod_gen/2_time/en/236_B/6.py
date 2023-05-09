def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(1, 4*N, 2):
        if A[i] != A[i-1]:
            print(A[i-1])
            break
        elif i == 4*N-1:
            print(A[i])

if __name__ == '__main__':
    main()