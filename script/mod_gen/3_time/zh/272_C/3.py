def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] == 0:
        print(-1)
    elif N == 2:
        if A[0] % 2 == 0:
            print(A[0])
        else:
            print(-1)
    else:
        if A[0] % 2 == 0:
            print(A[0])
        else:
            print(A[0] + A[1])
main()
