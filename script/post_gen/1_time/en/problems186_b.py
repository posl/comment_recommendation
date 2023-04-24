Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 100 * 100
    for h in range(H):
        for w in range(W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    cnt += abs(i - h) + abs(j - w) + A[i][j]
            ans = min(ans, cnt)
    print(ans)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    total = sum(sum(a) for a in A)
    if total % (H * W) != 0:
        print(-1)
        return
    n = total // (H * W)
    ans = 0
    for i in range(H):
        for j in range(W):
            if (i + j) % 2 == 0:
                ans += abs(A[i][j] - n)
    print(ans // 2)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    A_sum = sum(sum(a) for a in A)
    A_min = min(min(a) for a in A)
    print(A_sum - H * W * A_min)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    minA = min([min(Ai) for Ai in A])
    maxA = max([max(Ai) for Ai in A])
    minCount = 10000
    for i in range(minA, maxA+1):
        count = 0
        for j in range(H):
            for k in range(W):
                if A[j][k] > i:
                    count += A[j][k] - i
        minCount = min(minCount, count)
    print(minCount)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    A = [a for a in A if sum(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    if len(A[0]) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    A = [a for a in A if len(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    A = [a for a in A if len(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    A = [a for a in A if len(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    A = [a for a in A if len(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    A = [a for a in A if len(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    A = [a for a in A if len(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    A = [a for a in A if len(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    a_sum = sum([sum(i) for i in a])
    a_min = min([min(i) for i in a])
    print(a_sum - h*w*a_min)

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    #print(A)
    minA = min([min(a) for a in A])
    #print(minA)
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA
    print(ans)

=======
Suggestion 8

def main():
    # H,W = map(int, input().split())
    # A = [list(map(int, input().split())) for _ in range(H)]
    H, W = 3, 2
    A = [[4, 4], [4, 4], [4, 4]]
    A = [[99, 99, 99], [99, 0, 99], [99, 99, 99]]
    A = [[2, 2, 3], [3, 2, 2]]
    # print(A)
    # print(H, W)
    minA = min([min(a) for a in A])
    maxA = max([max(a) for a in A])
    # print(minA, maxA)
    minDiff = 10000
    for i in range(minA, maxA + 1):
        diff = 0
        for a in A:
            diff += sum([abs(i - j) for j in a])
        minDiff = min(diff, minDiff)
    print(minDiff)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    #print(A)
    minA = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < minA:
                minA = A[i][j]
    #print(minA)
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minA
    print(ans)

=======
Suggestion 10

def main():
    # Read data
    H, W = map(int, input().split())
    A = [[int(a) for a in input().split()] for _ in range(H)]

    # Find minimum number of blocks
    min_ = min([min(a) for a in A])
    ans = 0
    for a in A:
        ans += sum([i - min_ for i in a])

    # Print answer
    print(ans)
