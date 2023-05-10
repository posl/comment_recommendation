Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
        return
    k -= x // d
    x %= d
    if k % 2 == 0:
        print(x)
    else:
        print(d - x)

=======
Suggestion 2

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if k <= x // d:
        print(x - k * d)
    else:
        k -= x // d
        x %= d
        if k % 2 == 0:
            print(x)
        else:
            print(d - x)

=======
Suggestion 3

def solve():
    x, k, d = map(int, input().split())
    x = abs(x)

    if x >= k * d:
        print(x - k * d)
        return

    k -= x // d
    x %= d

    if k % 2 == 0:
        print(x)
    else:
        print(d - x)

=======
Suggestion 4

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x // d > k:
        print(x - k * d)
    else:
        if (k - x // d) % 2 == 0:
            print(x % d)
        else:
            print(d - x % d)

=======
Suggestion 5

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if k*d <= x:
        print(x-k*d)
        return
    y = x // d
    if (k-y) % 2 == 0:
        print(x - y*d)
    else:
        print(abs(x-(y+1)*d))

=======
Suggestion 6

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
    else:
        k -= x // d
        x %= d
        if k % 2 == 0:
            print(x)
        else:
            print(d - x)

=======
Suggestion 7

def get_min_abs(x, k, d):
    x = abs(x)
    if x >= k * d:
        return x - k * d
    else:
        k -= x // d
        x = x % d
        if k % 2 == 0:
            return x
        else:
            return d - x

x, k, d = map(int, input().split())
print(get_min_abs(x, k, d))

=======
Suggestion 8

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if k <= x // d:
        ans = x - k * d
    else:
        ans = x % d
        if (k - x // d) % 2 == 1:
            ans = d - ans
    print(ans)

=======
Suggestion 9

def main():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x // d >= k:
        print(x - d * k)
    else:
        k -= x // d
        x = x % d
        if k % 2 == 0:
            print(x)
        else:
            print(abs(x - d))
    return
