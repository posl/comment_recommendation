Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])

    last = 0
    for i in range(n):
        if ab[i][0] > last:
            last = ab[i][1] - 1

    print(last)

=======
Suggestion 2

def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[0])
    print(ab)
    m = 0
    for i in range(n):
        if ab[i][0] > m:
            print(ab[i][0])
            return
        m = max(m, ab[i][1])
    print(m)

=======
Suggestion 3

def check(n, a, b, x):
    for i in range(n):
        if a[i] <= x <= b[i] or b[i] <= x <= a[i]:
            continue
        else:
            return False
    return True

=======
Suggestion 4

def main():
    n = int(input())
    ab = []
    for _ in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[1])
    ab.sort(key=lambda x: x[0])
    ab.sort(key=lambda x: x[1] - x[0])

    #print(ab)
    now = 1
    for a, b in ab:
        if b <= now:
            continue
        else:
            now = b
    print(now)

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    if N == 1:
        print(max(A[0], B[0]))
        exit()

    A.sort()
    B.sort()
    if N % 2 == 0:
        l = N // 2
        r = l + 1
        ans = (B[l - 1] + B[r - 1]) - (A[l - 1] + A[r - 1]) + 1
    else:
        l = N // 2 + 1
        ans = B[l - 1] - A[l - 1] + 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 0:
        a = A[N // 2 - 1] + A[N // 2]
        b = B[N // 2 - 1] + B[N // 2]
        print(b - a + 1)
    else:
        print(B[N // 2] - A[N // 2] + 1)

=======
Suggestion 7

def main():
    N = int(input())
    #print(N)
    #print(type(N))
    A = []
    B = []
    for i in range(N):
        A_i, B_i = map(int, input().split())
        A.append(A_i)
        B.append(B_i)
    #print(A)
    #print(B)
    #print(type(A))
    #print(type(B))
    #print(max(A))
    #print(min(B))
    if max(A) <= min(B):
        print(min(B) - 1)
    else:
        print(-1)

=======
Suggestion 8

def find_max_floor(N, ladders):
    # print(N, ladders)
    if N == 1:
        return 1

    # ladders = sorted(ladders, key=lambda x: x[0])
    # print(ladders)

    # max_floor = 1
    # for i in range(len(ladders)):
    #     if ladders[i][0] > max_floor:
    #         return max_floor
    #     else:
    #         max_floor = max(max_floor, ladders[i][1])
    # return max_floor

    max_floor = 1
    ladders = sorted(ladders, key=lambda x: x[1])
    for i in range(len(ladders)):
        if ladders[i][1] > max_floor:
            return max_floor
        else:
            max_floor = max(max_floor, ladders[i][0])
    return max_floor

=======
Suggestion 9

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(min(B) - max(A) + 1 if min(B) - max(A) + 1 > 0 else 0)

=======
Suggestion 10

def main():
    # 读入
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    # 处理
    a_min = max(a)
    b_min = min(b)

    # 输出
    if a_min > b_min:
        print(0)
    else:
        print(b_min - a_min + 1)
