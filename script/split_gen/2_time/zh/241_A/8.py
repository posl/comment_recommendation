def main():
    n = int(input())
    a = list(map(int, input().split()))
    dict = {}
    for i in range(n):
        if a[i] not in dict:
            dict[a[i]] = 1
        else:
            dict[a[i]] += 1
    ans = 0
    for k in dict:
        if dict[k] >= k:
            ans += dict[k] - k
        else:
            ans += dict[k]
    print(ans)
