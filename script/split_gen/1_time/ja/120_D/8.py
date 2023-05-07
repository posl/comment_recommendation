def main():
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(M)]
    ab = sorted(ab, key=lambda x: x[1])
    #print(ab)
    ans = 0
    #print(ab[0][1])
    for i in range(M):
        #print(ab[i][0])
        if ab[i][0] < ab[i][1]:
            ans += 1
            #print(ans)
    print(ans)
