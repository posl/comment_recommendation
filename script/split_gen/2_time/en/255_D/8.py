def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for i in range(Q)]
    A.sort()
    A.append(0)
    A.append(10**9)
    A.sort()
    ans = 0
    for i in range(1, N+2):
        ans += (A[i]-A[i-1]) * (i-1) * (N-i+1)
    for x in X:
        print(ans + (x-A[0])*(N+1))
