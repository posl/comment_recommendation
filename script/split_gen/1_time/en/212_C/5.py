def main():
    import sys
    from bisect import bisect_left
    input = sys.stdin.readline
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    ans = 10**9
    for a in A:
        ind = bisect_left(B,a)
        if ind == 0:
            ans = min(ans,abs(a-B[0]))
        elif ind == M:
            ans = min(ans,abs(a-B[-1]))
        else:
            ans = min(ans,abs(a-B[ind]),abs(a-B[ind-1]))
    print(ans)
main()
I'm trying to solve this problem: https://atcoder.jp/contests/abc153/tasks/abc153_f
This is my code:
