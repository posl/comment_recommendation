def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            bag = V[:i] + V[N-j:]
            bag.sort()
            for k in range(min(K - i - j, len(bag))):
                if bag[k] < 0:
                    bag[k] = 0
            ans = max(ans, sum(bag))
    print(ans)
