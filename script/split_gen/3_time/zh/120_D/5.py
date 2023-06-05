def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    #print(AB)
    #print(N, M)
    #print(AB)
    ans = 0
    for i in range(M):
        a = AB[i][0]
        b = AB[i][1]
        if a > b:
            a, b = b, a
        if a == 1 and b == N:
            ans += 1
        elif a == 1 or b == N:
            ans += 2
        else:
            ans += 2
    print(ans)
