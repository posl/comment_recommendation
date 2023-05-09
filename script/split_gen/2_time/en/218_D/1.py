def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    #print(x)
    #print(y)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if x[i] == x[j]:
                    if y[i] == y[k] or y[j] == y[k]:
                        ans += 1
                elif x[i] == x[k]:
                    if y[i] == y[j] or y[j] == y[k]:
                        ans += 1
                elif x[j] == x[k]:
                    if y[i] == y[j] or y[i] == y[k]:
                        ans += 1
    print(ans)
