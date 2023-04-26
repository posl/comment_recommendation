Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    ans = min(ans, A[i][j] + A[k][l] + C * (abs(i-k) + abs(j-l)))
    print(ans)

=======
Suggestion 2

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    ans = min(ans, A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l)))
    print(ans)

=======
Suggestion 3

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    ans = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    else:
                        ans = min(ans, A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l)))
    print(ans)

=======
Suggestion 4

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    ans = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    ans = min(ans, A[i][j] + A[k][l] + C * (abs(i-k) + abs(j-l)))
    print(ans)

=======
Suggestion 5

def main():
    H, W, C = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    ans = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i != k or j != l:
                        ans = min(ans, A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l)))
    print(ans)

=======
Suggestion 6

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10**10
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    ans = min(ans, A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l)))
    print(ans)

=======
Suggestion 7

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h)]
    ans = 10**20
    for i in range(h):
        for j in range(w):
            for k in range(h):
                for l in range(w):
                    ans = min(ans, a[i][j] + a[k][l] + c * (abs(i - k) + abs(j - l)))
    print(ans)

=======
Suggestion 8

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    cost = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            cost[i][j] = A[i][j] + i + j

    ans = 10**18
    for i in range(H):
        for j in range(W):
            for k in range(H):
                for l in range(W):
                    if i == k and j == l:
                        continue
                    ans = min(ans, cost[i][j] + cost[k][l] + C * (abs(i-k) + abs(j-l)))
    print(ans)

=======
Suggestion 9

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10 ** 18
    for j in range(w):
        for i in range(h):
            for k in range(w):
                for l in range(h):
                    if (i, j) != (l, k):
                        ans = min(ans, a[i][j] + a[l][k] + c * (abs(i - l) + abs(j - k)))
    print(ans)

=======
Suggestion 10

def main():
    # input
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    # compute
    B = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            B[i][j] = A[i][j] - C*(i+j)

    # output
    print(min([min(B[i]) for i in range(H)]))
