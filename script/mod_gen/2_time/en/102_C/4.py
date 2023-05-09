def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N % 2 == 0:
        print(sum(A[N//2:]) - sum(A[:N//2]))
    else:
        print(min(sum(A[N//2+1:]) - sum(A[:N//2]), sum(A[N//2:]) - sum(A[:N//2-1])))

if __name__ == '__main__':
    main()