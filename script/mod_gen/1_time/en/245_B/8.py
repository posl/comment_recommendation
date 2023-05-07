def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != 0:
        print(0)
    else:
        for i in range(0, N-1):
            if A[i] + 1 < A[i+1]:
                print(A[i]+1)
                break
            elif i == N-2:
                print(A[i]+1)

if __name__ == '__main__':
    main()