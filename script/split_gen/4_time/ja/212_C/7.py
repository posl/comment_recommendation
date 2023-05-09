def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    min_diff = 10**9
    for i in range(n):
        diff = abs(a[i] - b[0])
        if diff < min_diff:
            min_diff = diff
        for j in range(m):
            diff = abs(a[i] - b[j])
            if diff < min_diff:
                min_diff = diff
            else:
                break
    print(min_diff)
