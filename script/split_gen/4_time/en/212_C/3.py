def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    i = 0
    j = 0
    min_diff = 10**9
    while i < n and j < m:
        if a[i] == b[j]:
            min_diff = 0
            break
        elif a[i] < b[j]:
            min_diff = min(min_diff, b[j] - a[i])
            i += 1
        else:
            min_diff = min(min_diff, a[i] - b[j])
            j += 1
    print(min_diff)
