Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    vl = list(map(int, input().split()))

    vl.sort()
    res = vl[0]
    for i in range(1, n):
        res = (res + vl[i]) / 2
    print(res)

=======
Suggestion 2

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = v[0]
    for i in range(1, n):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 3

def problems138_c():
    n = 3
    v = [500, 300, 200]
    v.sort()
    while len(v) > 1:
        x = v.pop(0)
        y = v.pop(0)
        v.append((x + y) / 2)
        v.sort()
    print(v[0])

=======
Suggestion 4

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = v[0]
    for i in range(1, N):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(n-1):
        v[i+1] = (v[i]+v[i+1])/2
    print(v[n-1])

=======
Suggestion 6

def main():
    num = int(input())
    values = list(map(int, input().split()))

    values.sort()
    result = values[0]
    for i in range(1, num):
        result = (result + values[i]) / 2

    print(result)

=======
Suggestion 7

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(N-1):
        v[i+1] = (v[i] + v[i+1]) / 2
    print(v[N-1])

=======
Suggestion 8

def main():
    N = int(input())
    v = [int(i) for i in input().split()]
    v.sort()
    res = v[0]
    for i in range(1, N):
        res = (res + v[i]) / 2
    print(res)

=======
Suggestion 9

def get_max_value(vals):
    if len(vals) == 1:
        return vals[0]
    else:
        vals.sort()
        return get_max_value(vals[1:]) + (vals[0] - vals[1]) / 2
