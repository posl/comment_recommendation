def binarySearch(x, l):
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        if l[mid] == x:
            return mid
        elif l[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return right
A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]
INF = 10**20
s = [-INF] + s + [INF]
t = [-INF] + t + [INF]
for i in range(Q):
    ans = INF
    a = binarySearch(x[i], s)
    b = binarySearch(x[i], t)
    for S in [s[a], s[a+1]]:
        for T in [t[b], t[b+1]]:
            d1 = abs(x[i] - S) + abs(S - T)
            d2 = abs(x[i] - T) + abs(T - S)
            ans = min(ans, d1, d2)
    print(ans)

if __name__ == '__main__':
    binarySearch()