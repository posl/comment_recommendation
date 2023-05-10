def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            a = x[i] - x[j]
            b = y[i] - y[j]
            count = 0
            for k in range(N):
                for l in range(k+1, N):
                    if x[k] - x[l] == a and y[k] - y[l] == b:
                        count += 1
            ans = max(ans, N - count)
    print(ans)
