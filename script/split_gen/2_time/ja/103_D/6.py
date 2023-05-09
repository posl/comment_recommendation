def main():
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(M)]
    ab = sorted(ab, key=lambda x: (x[0], -x[1]))
    #print(ab)
    ans = 0
    for i in range(M):
        a = ab[i][0]
        b = ab[i][1]
        for j in range(i+1, M):
            if ab[j][0] <= a and b <= ab[j][1]:
                ans += 1
                break
    print(ans)
