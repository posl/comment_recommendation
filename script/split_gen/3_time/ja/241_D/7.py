def main():
    import sys
    input = sys.stdin.readline
    from bisect import bisect_left, bisect_right
    Q = int(input())
    A = []
    ans = []
    for i in range(Q):
        c, *x = map(int, input().split())
        if c == 1:
            A.append(x[0])
        elif c == 2:
            a = bisect_left(A, x[0])
            if len(A) - a < x[1]:
                ans.append(-1)
            else:
                ans.append(A[a+x[1]-1])
        else:
            a = bisect_right(A, x[0])
            if a < x[1]:
                ans.append(-1)
            else:
                ans.append(A[a-x[1]])
    for i in ans:
        print(i)
