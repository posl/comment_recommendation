def main():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    def dfs(city, visited, time):
        if visited == (1 << n) - 1:
            return time + t[city][0] == k
        else:
            return sum(dfs(i, visited | (1 << i), time + t[city][i]) for i in range(n) if not visited >> i & 1)
    print(dfs(0, 1, 0))
