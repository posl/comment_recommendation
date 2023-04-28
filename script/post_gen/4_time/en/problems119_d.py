Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    S.append(10**20)
    S.append(-10**20)
    T.append(10**20)
    T.append(-10**20)
    S.sort()
    T.sort()
    for x in X:
        s = S[bisect.bisect_left(S, x)]
        t = T[bisect.bisect_left(T, x)]
        ans = 10**20
        for si in [s-1, s]:
            for ti in [t-1, t]:
                ans = min(ans, abs(x-si)+abs(si-ti), abs(x-ti)+abs(si-ti))
        print(ans)

=======
Suggestion 2

def main():
    A, B, Q = map(int, input().split())
    s = [-10**20] + [int(input()) for _ in range(A)] + [10**20]
    t = [-10**20] + [int(input()) for _ in range(B)] + [10**20]
    x = [int(input()) for _ in range(Q)]
    for i in x:
        s_index = bisect.bisect_left(s, i)
        t_index = bisect.bisect_left(t, i)
        ans = 10**20
        for j in [s[s_index-1], s[s_index]]:
            for k in [t[t_index-1], t[t_index]]:
                ans = min(ans, max(i-j, 0) + max(k-i, 0), max(i-k, 0) + max(j-i, 0))
        print(ans)

=======
Suggestion 3

def main():
    A, B, Q = map(int, input().split())
    s = [-10**20] + [int(input()) for _ in range(A)] + [10**20]
    t = [-10**20] + [int(input()) for _ in range(B)] + [10**20]
    x = [int(input()) for _ in range(Q)]
    for xi in x:
        ans = 10**20
        for si in s:
            for ti in t:
                if si <= xi and xi <= ti:
                    ans = min(ans, abs(xi - si) + abs(ti - si))
                elif si <= xi and xi <= ti:
                    ans = min(ans, abs(xi - ti) + abs(si - ti))
                elif si <= xi and xi <= ti:
                    ans = min(ans, abs(xi - si) + abs(ti - si))
                else:
                    ans = min(ans, abs(xi - si) + abs(ti - si))
        print(ans)

=======
Suggestion 4

def main():
    A, B, Q = map(int, input().split())
    s = [-10**12] + [int(input()) for _ in range(A)] + [10**12]
    t = [-10**12] + [int(input()) for _ in range(B)] + [10**12]
    x = [int(input()) for _ in range(Q)]

    for i in x:
        s_idx = bisect.bisect_right(s, i)
        t_idx = bisect.bisect_right(t, i)
        ans = 10**12
        for j in range(s_idx - 1, s_idx + 1):
            for k in range(t_idx - 1, t_idx + 1):
                ans = min(ans, abs(i - s[j]) + abs(s[j] - t[k]), abs(i - t[k]) + abs(t[k] - s[j]))
        print(ans)

=======
Suggestion 5

def main():
    a, b, q = map(int, input().split())
    s = [-10**20] + [int(input()) for _ in range(a)] + [10**20]
    t = [-10**20] + [int(input()) for _ in range(b)] + [10**20]
    x = [int(input()) for _ in range(q)]
    for i in range(q):
        si = bisect.bisect_left(s, x[i])
        ti = bisect.bisect_left(t, x[i])
        ans = 10**20
        for j in range(si-1, si+1):
            for k in range(ti-1, ti+1):
                ans = min(ans, max(s[j], t[k]) - x[i])
                ans = min(ans, x[i] - min(s[j], t[k]))
        print(ans)

=======
Suggestion 6

def main():
    a, b, q = map(int, input().split())
    s = [-10 ** 20] + [int(input()) for _ in range(a)] + [10 ** 20]
    t = [-10 ** 20] + [int(input()) for _ in range(b)] + [10 ** 20]
    for _ in range(q):
        x = int(input())
        si = bisect.bisect_left(s, x)
        ti = bisect.bisect_left(t, x)
        ans = 10 ** 20
        for j in range(ti - 1, ti + 1):
            for i in range(si - 1, si + 1):
                ans = min(ans, max(s[i] - x, x - t[j]), max(t[j] - x, x - s[i]))
        print(ans)

=======
Suggestion 7

def main():
    A,B,Q = map(int,input().split())
    s = [-10**10] + [int(input()) for _ in range(A)] + [10**10]
    t = [-10**10] + [int(input()) for _ in range(B)] + [10**10]
    x = [int(input()) for _ in range(Q)]
    for i in x:
        a = bisect.bisect_left(s,i)
        b = bisect.bisect_left(t,i)
        ans = 10**20
        for j in range(a-1,a+1):
            for k in range(b-1,b+1):
                ans = min(ans,abs(i-s[j])+abs(s[j]-t[k]),abs(i-t[k])+abs(t[k]-s[j]))
        print(ans)

import bisect
main()

=======
Suggestion 8

def binary_search(A, x):
    left = -1
    right = len(A)
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] <= x:
            left = mid
        else:
            right = mid
    return left

=======
Suggestion 9

def solve():
    A, B, Q = [int(i) for i in input().split()]
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    s = [-float("inf")] + s + [float("inf")]
    t = [-float("inf")] + t + [float("inf")]
    for i in x:
        s_idx = bisect_left(s, i)
        t_idx = bisect_left(t, i)
        ans = float("inf")
        for j in [s[s_idx-1], s[s_idx]]:
            for k in [t[t_idx-1], t[t_idx]]:
                if j <= i and i <= k:
                    ans = min(ans, max(i-j, k-i))
                else:
                    ans = min(ans, abs(i-j) + abs(j-k), abs(i-k) + abs(k-j))
        print(ans)
solve()

=======
Suggestion 10

def get_distance_from_shrine(shrine, shrine_list):
    left = 0
    right = len(shrine_list) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if shrine_list[mid] == shrine:
            return 0
        elif shrine_list[mid] < shrine:
            left = mid + 1
        else:
            right = mid - 1
    if right < 0:
        return shrine_list[0] - shrine
    if left >= len(shrine_list):
        return shrine - shrine_list[-1]
    return min(shrine_list[left] - shrine, shrine - shrine_list[right])
