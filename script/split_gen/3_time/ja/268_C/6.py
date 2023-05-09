def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    P = list(map(int, input().split()))
    A = [0]*N
    for i in range(N):
        A[P[i]] = i
    #print(A)
    #print(P)
    ans = 1
    for i in range(N-1):
        if A[i+1] - A[i] == 1:
            pass
        else:
            ans += 1
    print(ans)
