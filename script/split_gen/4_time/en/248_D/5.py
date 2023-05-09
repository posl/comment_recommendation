def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    ans = [0]*Q
    for i in range(Q):
        L, R, X = map(int, input().split())
        for j in range(L-1, R):
            if A[j] == X:
                ans[i] += 1
    for i in range(Q):
        print(ans[i])
