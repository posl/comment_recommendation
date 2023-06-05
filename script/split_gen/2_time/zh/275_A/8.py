def solve():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.append(0)
    if N == 1:
        if A[0] == x and A[1] == y:
            print("Yes")
        else:
            print("No")
    else:
        for i in range(N):
            for j in range(i + 1, N + 1):
                if A[i] + A[j] == abs(x - y):
                    print("Yes")
                    return
        print("No")
