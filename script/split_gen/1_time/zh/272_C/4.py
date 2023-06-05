def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[N-1] % 2 == 0:
        print(A[N-1])
        return
    else:
        for i in range(N-1):
            if A[i] % 2 == 0:
                print(A[N-1] + A[i])
                return
    print(-1)
    return
main()
