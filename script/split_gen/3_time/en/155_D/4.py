def main():
    from sys import stdin
    from bisect import bisect_left
    _ = [int(x) for x in stdin.readline().split()]
    N = _[0]
    K = _[1]
    A = [int(x) for x in stdin.readline().split()]
    A.sort()
    #print(A)
    def count_less_than_or_equal_to(x):
        #print("x=",x)
        count = 0
        for i in range(N):
            if A[i] == 0:
                if x >= 0:
                    count += N
                break
            elif A[i] < 0:
                if x >= 0:
                    count += N - bisect_left(A, -(-x//A[i]))
                else:
                    count += bisect_left(A, -(-x//A[i]))
            else:
                if x >= 0:
                    count += bisect_left(A, x//A[i])
                else:
                    count += N - bisect_left(A, -(-x//A[i]))
        #print("count=",count)
        return count
    ok = -10**18
    ng = 10**18
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if count_less_than_or_equal_to(mid) >= K:
            ng = mid
        else:
            ok = mid
    print(ng)
