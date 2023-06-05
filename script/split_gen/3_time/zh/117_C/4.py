def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    else:
        x_diff = []
        for i in range(1, m):
            x_diff.append(x[i] - x[i-1])
        x_diff.sort(reverse=True)
        print(sum(x_diff[n-1:]))
