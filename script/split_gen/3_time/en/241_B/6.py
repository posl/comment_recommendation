def main():
    import sys
    from bisect import bisect_left
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    for b in B:
        i = bisect_left(A, b)
        if i == N or A[i] != b:
            print("No")
            return
        del A[i]
    print("Yes")
