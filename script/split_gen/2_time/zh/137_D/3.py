def main():
    N, M = map(int, input().split())
    works = []
    for i in range(N):
        works.append(tuple(map(int, input().split())))
    works.sort(key=lambda x:x[0])
    ans = 0
    day = 0
    for i in range(N):
        if day + works[i][0] <= M:
            ans += works[i][1]
            day += works[i][0]
    print(ans)
