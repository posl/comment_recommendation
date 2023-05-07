def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    a = 0
    b = 0
    while a < N and b < M:
        if A[a] < B[b]:
            a += 1
        elif A[a] == B[b]:
            a += 1
            b += 1
        else:
            print("No")
            return
    if b == M:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()