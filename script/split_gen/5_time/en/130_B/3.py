def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    cnt = 0
    for d in D:
        if d <= X:
            cnt += 1
    print(cnt)
