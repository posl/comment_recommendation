def main():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    a.sort(reverse=True)
    b.sort(reverse=True)
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum < b_sum:
        print(0)
        return
    i = 0
    j = 0
    ans = 0
    while i < n and j < n:
        if a[i] > b[j]:
            ans += 1
            i += 1
        else:
            j += 1
    print(ans+1)
