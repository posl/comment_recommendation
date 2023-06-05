def main():
    n,m = input().split()
    n = int(n)
    m = int(m)
    cakes = []
    for i in range(n):
        cakes.append(list(map(int,input().split())))
    cakes.sort(key=lambda x:abs(x[0])+abs(x[1])+abs(x[2]),reverse=True)
    ans = 0
    for i in range(m):
        ans += abs(cakes[i][0]) + abs(cakes[i][1]) + abs(cakes[i][2])
    print(ans)
