Synthesizing 10/10 solutions

=======
Suggestion 1

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
        ans = B[N//2] - A[N//2] + 1
    else:
        ans = B[N//2] - A[N//2] + 1
    print(ans)

=======
Suggestion 2

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
    if N % 2 == 1:
        ans = B[N // 2] - A[N // 2] + 1
    else:
        ans = B[N // 2] - A[N // 2]
        ans += B[N // 2 - 1] - A[N // 2 - 1] + 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort(reverse=True)
    B.sort(reverse=True)
    a = A[0]
    b = B[0]
    if a != b:
        print(a+b)
    else:
        a2 = A[1]
        b2 = B[1]
        print(max(a+a2, b+b2))

=======
Suggestion 4

def main():
    N = int(input())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())

    a.sort()
    b.sort()
    if N % 2 == 0:
        ans = b[N // 2] - a[N // 2 - 1] + 1
    else:
        ans = b[N // 2] - a[N // 2] + 1
    print(ans)

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
    print(max(max(A), max(B)))

=======
Suggestion 6

def main():
    N = int(input())
    L = []
    for _ in range(N):
        a, b = map(int, input().split())
        L.append((a, b))
    L.sort(key=lambda x: x[0])
    ans = 0
    for a, b in L:
        ans = max(ans, b)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 階を昇順にソート
    A, B = zip(*sorted(zip(A, B)))
    A, B = list(A), list(B)

    # はしごの上の階を取得
    up = A[-1]
    # はしごの下の階を取得
    down = B[0]

    # 上の階が下の階よりも高い場合
    if up > down:
        # 上の階を出力
        print(up)
    # 上の階が下の階よりも低い場合
    else:
        # 1を出力
        print(1)

=======
Suggestion 8

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    ans = 1
    for a, b in AB:
        if ans < a:
            ans = a
        ans = b
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])

    ans = 1
    for a, b in AB:
        if ans < a:
            break
        ans = max(ans, b)
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # print(N, AB)
    # print(AB[0][0], AB[0][1])
    # print(AB[1][0], AB[1][1])
    # print(AB[2][0], AB[2][1])
    # print(AB[3][0], AB[3][1])
    # print(AB[4][0], AB[4][1])
    # print(AB[5][0], AB[5][1])
    # print(AB[6][0], AB[6][1])
    # print(AB[7][0], AB[7][1])
    # print(AB[8][0], AB[8][1])
    # print(AB[9][0], AB[9][1])
    # print(AB[10][0], AB[10][1])
    # print(AB[11][0], AB[11][1])
    # print(AB[12][0], AB[12][1])
    # print(AB[13][0], AB[13][1])
    # print(AB[14][0], AB[14][1])
    # print(AB[15][0], AB[15][1])
    # print(AB[16][0], AB[16][1])
    # print(AB[17][0], AB[17][1])
    # print(AB[18][0], AB[18][1])
    # print(AB[19][0], AB[19][1])
    # print(AB[20][0], AB[20][1])
    # print(AB[21][0], AB[21][1])
    # print(AB[22][0], AB[22][1])
    # print(AB[23][0], AB[23][1])
    # print(AB[24][0], AB[24][1])
    # print(AB[25][0], AB[25][1])
    # print(AB[26][0], AB[26][1])
    # print(AB[27][0], AB[27][1])
    # print(AB[28][0], AB[28][1])
    # print
