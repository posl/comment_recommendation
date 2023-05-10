def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    now = 0
    for x, y in XY:
        T -= x - now
        if T <= 0:
            print("No")
            return
        T += y - x
        now = y
        if T > A[N-2]:
            T = A[N-2]
    T -= N - 1 - now
    if T <= 0:
        print("No")
        return
    print("Yes")
