def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    while A:
        if abs(A.pop() - B.pop()) > K:
            print("No")
            return
    print("Yes")
    return
