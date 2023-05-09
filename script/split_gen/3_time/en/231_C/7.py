def main():
    #input
    N, Q = map(int, input().split())
    As = list(map(int, input().split()))
    xs = [int(input()) for _ in range(Q)]
    #process
    As.sort()
    As = [0] + As
    for i in range(N):
        As[i+1] += As[i]
    for x in xs:
        #binary search
        ng = -1
        ok = N+1
        while ok - ng > 1:
            mid = (ok + ng) // 2
            if As[mid] >= x*(N-mid+1):
                ok = mid
            else:
                ng = mid
        print(N-ok+1)
