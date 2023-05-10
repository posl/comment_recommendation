def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    min_diff = None
    for i in range(n):
        for j in range(m):
            diff = abs(a[i] - b[j])
            if min_diff is None or diff < min_diff:
                min_diff = diff
    print(min_diff)
