def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    right = -1
    for i in range(M):
        if AB[i][0] > right:
            ans += 1
            right = AB[i][1]
    print(ans)
