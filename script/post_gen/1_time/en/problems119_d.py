Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, q = map(int, input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]
    for i in range(q):
        ans = 10**18
        for j in range(a):
            for k in range(b):
                ans = min(ans, abs(s[j] - x[i]) + abs(t[k] - s[j]))
                ans = min(ans, abs(t[k] - x[i]) + abs(s[j] - t[k]))
        print(ans)

=======
Suggestion 2

def main():
    A, B, Q = map(int, input().split())
    S = [-float('inf')] + [int(input()) for _ in range(A)] + [float('inf')]
    T = [-float('inf')] + [int(input()) for _ in range(B)] + [float('inf')]
    X = [int(input()) for _ in range(Q)]

    for x in X:
        s = bisect.bisect_right(S, x)
        t = bisect.bisect_right(T, x)
        ans = float('inf')
        for si in [s - 1, s]:
            for ti in [t - 1, t]:
                ans = min(ans, max(S[si], T[ti]) - x, x - min(S[si], T[ti]))
                ans = min(ans, abs(S[si] - x) + abs(T[ti] - S[si]))
                ans = min(ans, abs(T[ti] - x) + abs(S[si] - T[ti]))
        print(ans)

=======
Suggestion 3

def main():
    A, B, Q = map(int, input().split())
    s = [-10**10] + [int(input()) for _ in range(A)] + [10**10]
    t = [-10**10] + [int(input()) for _ in range(B)] + [10**10]
    x = [int(input()) for _ in range(Q)]
    for i in x:
        s1 = s[bisect.bisect_left(s, i)-1]
        s2 = s[bisect.bisect_left(s, i)]
        t1 = t[bisect.bisect_left(t, i)-1]
        t2 = t[bisect.bisect_left(t, i)]
        print(min(abs(i-s1)+abs(s1-t1), abs(i-s1)+abs(s1-t2), abs(i-s2)+abs(s2-t1), abs(i-s2)+abs(s2-t2)))

=======
Suggestion 4

def main():
    A, B, Q = map(int, input().split())
    s = [-10**10] + [int(input()) for _ in range(A)] + [10**10]
    t = [-10**10] + [int(input()) for _ in range(B)] + [10**10]
    x = [int(input()) for _ in range(Q)]
    for i in range(Q):
        si = bisect.bisect_left(s, x[i])
        ti = bisect.bisect_left(t, x[i])
        ans = 10**20
        for a in [s[si-1], s[si]]:
            for b in [t[ti-1], t[ti]]:
                ans = min(ans, max(a, b)-x[i], x[i]-min(a, b))
        print(ans)

=======
Suggestion 5

def main():
    A, B, Q = map(int, input().split())
    s = [-10**10] + [int(input()) for _ in range(A)] + [10**10]
    t = [-10**10] + [int(input()) for _ in range(B)] + [10**10]
    x = [int(input()) for _ in range(Q)]
    for i in x:
        s_i = bisect.bisect_right(s, i)
        t_i = bisect.bisect_right(t, i)
        s_l = s[s_i-1]
        s_r = s[s_i]
        t_l = t[t_i-1]
        t_r = t[t_i]
        dist = min(abs(i-s_l)+abs(t_l-s_l), abs(i-s_l)+abs(t_r-s_l), abs(i-s_r)+abs(t_l-s_r), abs(i-s_r)+abs(t_r-s_r))
        print(dist)

=======
Suggestion 6

def main():
    A, B, Q = map(int, input().split())
    s = [-10**15] + [int(input()) for _ in range(A)] + [10**15]
    t = [-10**15] + [int(input()) for _ in range(B)] + [10**15]
    x = [int(input()) for _ in range(Q)]

    for i in x:
        s_index = bisect.bisect_right(s, i)
        t_index = bisect.bisect_right(t, i)
        ans = 10**15
        for j in range(s_index-1, s_index+1):
            for k in range(t_index-1, t_index+1):
                ans = min(ans, max(s[j]-i, i-t[k]), max(t[k]-i, i-s[j]))
        print(ans)

=======
Suggestion 7

def main():
    a, b, q = map(int, input().split())
    s = [-10**15] + [int(input()) for _ in range(a)] + [10**15]
    t = [-10**15] + [int(input()) for _ in range(b)] + [10**15]
    x = [int(input()) for _ in range(q)]
    for i in range(q):
        ans = 10**15
        for j in range(a + 2):
            if s[j] >= x[i]:
                break
        for k in range(b + 2):
            if t[k] >= x[i]:
                break
        for l in range(j - 1, j + 1):
            for m in range(k - 1, k + 1):
                ans = min(ans, max(s[l] - x[i], x[i] - t[m]))
                ans = min(ans, max(t[m] - x[i], x[i] - s[l]))
        print(ans)

main()

=======
Suggestion 8

def main():
    A, B, Q = list(map(int, input().split()))
    s = [-10**11] + [int(input()) for _ in range(A)] + [10**11]
    t = [-10**11] + [int(input()) for _ in range(B)] + [10**11]
    x = [int(input()) for _ in range(Q)]
    for i in range(Q):
        ans = 10**20
        for j in range(A+2):
            if s[j] > x[i]:
                break
        for k in range(B+2):
            if t[k] > x[i]:
                break
        for l in range(j-1, j+1):
            for m in range(k-1, k+1):
                ans = min(ans, max(s[l]-x[i], x[i]-t[m]))
                ans = min(ans, max(t[m]-x[i], x[i]-s[l]))
        print(ans)

=======
Suggestion 9

def binary_search(arr, val):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == val:
            return m
        elif arr[m] > val:
            r = m - 1
        else:
            l = m + 1
    return l

=======
Suggestion 10

def get_closest_shrine temples, shrine
  temples.each do |temple|
    if shrine < temple
      return shrine
    end
  end
  return temples.last
end
