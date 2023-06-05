def solution():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    #print(ab)
    ans = 1
    for i in range(n):
        if ab[i][0] < ans <= ab[i][1]:
            ans = ab[i][1] + 1
    print(ans)
