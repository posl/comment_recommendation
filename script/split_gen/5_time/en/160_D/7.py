def main():
    #import sys
    #f = open('test.txt', 'r')
    #sys.stdin = f
    N, X, Y = map(int, input().split())
    ans = [0] * (N-1)
    for i in range(1, N):
        for j in range(i+1, N+1):
            if j - i <= X:
                ans[j-i-1] += 1
            elif i <= X and j > X and j - i <= Y:
                ans[min(j-X-1, i-1+Y-X)] += 1
            elif i > X and j > X and j - i <= Y:
                ans[min(j-i-1, i-X-1+Y-X)] += 1
            else:
                ans[min(j-i-1, i-X-1+Y-X)] += 1
                ans[min(j-i-1, i-1+Y-X)] += 1
    for i in range(N-1):
        print(ans[i])
