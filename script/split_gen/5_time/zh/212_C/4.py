def main():
    n = int(input().split()[0])
    a = list(map(int, input().split()))
    m = int(input().split()[0])
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    i = 0
    j = 0
    ans = 10 ** 9
    while i < n and j < m:
        ans = min(ans, abs(a[i] - b[j]))
        if a[i] > b[j]:
            j += 1
        else:
            i += 1
    print(ans)
