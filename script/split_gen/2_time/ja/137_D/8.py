def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    #print(AB)
    ans = 0
    i = 0
    for j in range(1, M+1):
        while i < N and AB[i][0] == j:
            ans += AB[i][1]
            i += 1
        print(ans)
