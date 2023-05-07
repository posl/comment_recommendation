def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            x = X[i] - X[j]
            y = Y[i] - Y[j]
            for k in range(N):
                if k == i or k == j:
                    continue
                if x + X[k] == X[j] and y + Y[k] == Y[j]:
                    break
            else:
                ans += 1
    print(ans//3)
