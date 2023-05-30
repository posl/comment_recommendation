def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    i = 0
    k = 0
    ans = [0] * n
    while i < n:
        j = i
        while j < n and a[i] == a[j]:
            j += 1
        if j == n:
            ans[k] += n - i
            break
        ans[k] += j - i
        i = j
        k += 1
    print('\n'.join(map(str, ans)))
main()
