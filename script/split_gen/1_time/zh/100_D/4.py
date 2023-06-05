def main():
    n, m = map(int, input().split())
    cakes = []
    for i in range(n):
        cakes.append(list(map(int, input().split())))
    cakes.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    ans = 0
    for i in range(m):
        for j in range(m):
            for k in range(m):
                if i + j + k <= m:
                    sum = 0
                    for l in range(i):
                        sum += cakes[l][0]
                    for l in range(j):
                        sum += cakes[l][1]
                    for l in range(k):
                        sum += cakes[l][2]
                    ans = max(ans, abs(sum))
    print(ans)
