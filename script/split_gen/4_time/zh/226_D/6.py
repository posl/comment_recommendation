def main():
    n = int(input())
    x = [0]*n
    y = [0]*n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    ans = 1
    for i in range(n-1):
        for j in range(i+1, n):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            cnt = 0
            for k in range(n):
                for l in range(k+1, n):
                    if x[k] - x[l] == dx and y[k] - y[l] == dy:
                        cnt += 1
            ans = max(ans, cnt)
    print(n - ans)
