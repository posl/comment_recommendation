Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h, w, a, b = map(int, input().split())
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for k in range(h):
                if i >> k & 1:
                    cnt += 1
            for l in range(w):
                if j >> l & 1:
                    cnt += 1
            if cnt == a:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W, A, B = map(int, input().split())

    def dfs(i, bit, A, B):
        if i == H * W:
            return 1

        if bit >> i & 1:
            return dfs(i + 1, bit, A, B)

        res = 0

        if B:
            res += dfs(i + 1, bit | 1 << i, A, B - 1)

        if A:
            if i % W != W - 1 and not bit & 1 << (i + 1):
                res += dfs(i + 1, bit | 1 << i | 1 << (i + 1), A - 1, B)

            if i + W < H * W:
                res += dfs(i + 1, bit | 1 << i | 1 << (i + W), A - 1, B)

        return res

    print(dfs(0, 0, A, B))

=======
Suggestion 3

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 4

def main():
    H, W, A, B = map(int, input().split())
    print(solve(H, W, A, B))

=======
Suggestion 5

def main():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)

=======
Suggestion 6

def main():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)
    print(H, W, A, B)

=======
Suggestion 7

def main():
    H, W, A, B = map(int, input().split())
    print(0)

=======
Suggestion 8

def main():
    h, w, a, b = map(int, input().split())
    print(h, w, a, b)
    print('hello')

=======
Suggestion 9

def main():
    H, W, A, B = map(int, input().split())
    print("Hello World")
