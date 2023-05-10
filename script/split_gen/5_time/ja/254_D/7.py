def main():
    n = int(input())
    sq = []
    for i in range(1, int(n ** 0.5) + 1):
        sq.append(i ** 2)
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j in sq:
                ans += 1
    print(ans)
