def main():
    # n, m = map(int, input().split())
    # a = list(map(int, input().split()))
    # b = list(map(int, input().split()))
    n, m = 6, 8
    a = [82, 76, 82, 82, 71, 70]
    b = [17, 39, 67, 2, 45, 35, 22, 24]
    a.sort()
    b.sort()
    # print(a)
    # print(b)
    min_diff = 10**9
    i = 0
    for j in range(m):
        while i < n-1 and abs(a[i]-b[j]) > abs(a[i+1]-b[j]):
            i += 1
        min_diff = min(min_diff, abs(a[i]-b[j]))
    print(min_diff)
