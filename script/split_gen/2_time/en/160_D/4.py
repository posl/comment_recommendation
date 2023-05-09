def main():
    N, X, Y = map(int, input().split())
    ans = [0 for i in range(N-1)]
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            d = min(j-i, abs(X-i)+1+abs(Y-j))
            ans[d-1] += 1
    for a in ans:
        print(a)
