def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    i = 0
    j = n - 1
    while i < j:
        if a[i] == a[i + 1]:
            i += 2
        else:
            i += 1
        if a[j] == a[j - 1]:
            j -= 2
        else:
            j -= 1
        ans += 1
    if i == j:
        ans += 1
    print(ans)
