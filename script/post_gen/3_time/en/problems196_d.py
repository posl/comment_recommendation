Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(h, w, a, b):
    if a == 0 or b == 0:
        return 1
    return solve(h, w, a - 1, b) + solve(h, w, a, b - 1)

h, w, a, b = map(int, input().split())
print(solve(h, w, a, b))

=======
Suggestion 2

def main():
    H, W, A, B = map(int, input().s

=======
Suggestion 3

def main():
    H, W, A, B = map(int, input().split())
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            cnt = 0
            for k in range(H):
                if (i >> k) & 1 == 1:
                    continue
                for l in range(W):
                    if (j >> l) & 1 == 1:
                        continue
                    cnt += 1
            if cnt == A:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)

=======
Suggestion 5

def main():
    H, W, A, B = map(int, input().split())
    print(0)

=======
Suggestion 6

def solve():
    H, W, A, B = map(int, input().split())
    return 0

print(solve())

=======
Suggestion 7

def main():
    H, W, A, B = map(int, input().split())
    print(H,W,A,B)
    print('Hello World!')
    return

=======
Suggestion 8

def problem():
  H, W, A, B = map(int, input().split())
  print(H*W)

=======
Suggestion 9

def main():
    print('Hello')
    return
