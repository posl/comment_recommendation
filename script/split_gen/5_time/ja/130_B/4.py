def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    ans = 1
    for d in D:
        if d <= X:
            ans += 1
    print(ans)
