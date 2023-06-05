def main():
    n = int(input())
    a = list(map(int, input().split()))
    sums = [0]
    for i in range(n):
        sums.append(sums[-1] + a[i])
    def get_diff(i, j):
        return abs(sums[j] - sums[i])
    def get_max_diff(i, j):
        return max(get_diff(i, j), get_diff(j, i))
    ans = 10**9
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            ans = min(ans, max(get_max_diff(0, i), max(get_max_diff(i, j), get_max_diff(j, n))))
    print(ans)
