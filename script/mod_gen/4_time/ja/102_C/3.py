def get_ans(n, a):
    a.sort()
    b = a[n//2]
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (b+i))
    return ans
n = int(input())
a = list(map(int, input().split()))
print(get_ans(n, a))
