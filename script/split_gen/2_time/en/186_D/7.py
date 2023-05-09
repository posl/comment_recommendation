def main():
    import sys
    from collections import defaultdict
    from itertools import accumulate
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A_acc = list(accumulate(A))
    A_acc_r = list(accumulate(A[::-1]))[::-1]
    ans = 0
    for i in range(N-1):
        ans += (i+1)*A[i] - A_acc[i] + A_acc_r[i+1] - (N-i-1)*A[i+1]
    print(ans)
