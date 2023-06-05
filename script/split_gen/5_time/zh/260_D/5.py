def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    cards = [0] * n
    for i in range(n):
        cards[i] = [p[i], i]
    cards.sort(key=lambda x: x[0])
    ans = [-1] * n
    for i in range(k):
        ans[cards[i][1]] = i + 1
    print(*ans, sep='\n')
