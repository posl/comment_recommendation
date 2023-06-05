def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    res = 0
    for i in range(N):
        if A[i] > res:
            res = A[i]
        elif A[i] < res:
            res = A[i] - 1
        else:
            pass
    print(res)
main()
