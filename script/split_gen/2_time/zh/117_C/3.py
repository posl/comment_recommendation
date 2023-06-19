def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n == 1:
        print(abs(x[0]))
    else:
        x_diff = []
        for i in range(m - 1):
            x_diff.append(abs(x[i + 1] - x[i]))
        x_diff.sort()
        print(sum(x_diff[:n - 1]))
