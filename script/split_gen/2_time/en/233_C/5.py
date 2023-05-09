def main():
    N, X = map(int, input().split())
    L = []
    for _ in range(N):
        L.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, 1<<N):
        cnt = 0
        num = 1
        for j in range(N):
            if i>>j & 1:
                cnt += 1
                num *= L[j][cnt]
        if num == X:
            ans += 1
    print(ans)
