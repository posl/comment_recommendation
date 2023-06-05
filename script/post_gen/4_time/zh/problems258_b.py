Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def get_max_num(list):
    max_num = 0
    for i in range(len(list)):
        max_num += list[i] * (10 ** (len(list) - i - 1))
    return max_num

=======
Suggestion 3

def main():
    n = int(input())
    a = [list(map(int, input())) for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(n):
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0:
                        continue

                    x, y = i, j
                    num = 0
                    while True:
                        num *= 10
                        num += a[x][y]
                        x += di
                        y += dj
                        if x < 0 or x >= n or y < 0 or y >= n:
                            break

                    ans = max(ans, num)

    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = [list(map(int, input())) for _ in range(n)]
    ans = -1
    for i in range(n):
        for j in range(n):
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0:
                        continue
                    x, y = i, j
                    num = a[x][y]
                    for _ in range(n - 1):
                        x += di
                        y += dj
                        if not (0 <= x < n and 0 <= y < n):
                            break
                        num = num * 10 + a[x][y]
                    ans = max(ans, num)
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(8):
                ni = i
                nj = j
                tmp = ''
                for l in range(n):
                    if not (0 <= ni < n and 0 <= nj < n):
                        break
                    tmp += a[ni][nj]
                    ni += di[k]
                    nj += dj[k]
                ans = max(ans, int(tmp))
    print(ans)

di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input())))
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(8):
                ni = i
                nj = j
                tmp = 0
                for l in range(N):
                    tmp *= 10
                    tmp += A[ni][nj]
                    if k & 1:
                        ni = 2 * i - ni
                    else:
                        ni = 2 * i + ni
                    if k & 2:
                        nj = 2 * j - nj
                    else:
                        nj = 2 * j + nj
                    if ni < 0 or N <= ni or nj < 0 or N <= nj:
                        break
                ans = max(ans, tmp)
    print(ans)

=======
Suggestion 7

def get_max_num(n, nums):
    max_num = 0
    for i in range(n):
        for j in range(n):
            tmp = get_max_num_by_start(n, nums, i, j)
            if tmp > max_num:
                max_num = tmp
    return max_num

=======
Suggestion 8

def main():
    n = int(input())
    a = [list(map(int, input())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            p = a[i][j]
            for k in range(n):
                for l in range(n):
                    q = a[k][l]
                    b = [[0] * n for _ in range(n)]
                    b[i][j] = 1
                    b[k][l] = 1
                    for m in range(n):
                        for o in range(n):
                            if b[m][o] == 1:
                                continue
                            if (m == 0 or b[m - 1][o]) and (m == n - 1 or b[m + 1][o]) and (o == 0 or b[m][o - 1]) and (o == n - 1 or b[m][o + 1]):
                                b[m][o] = 1
                    t = 0
                    for m in range(n):
                        for o in range(n):
                            if b[m][o] == 1:
                                t += a[m][o]
                    ans = max(ans, t - p - q)
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input())))
    ans = -1
    for i in range(n):
        for j in range(n):
            for k in range(8):
                d = 10 ** 9
                ni = i
                nj = j
                for l in range(n):
                    ni += di[k]
                    nj += dj[k]
                    if ni == -1:
                        ni = n - 1
                    elif ni == n:
                        ni = 0
                    if nj == -1:
                        nj = n - 1
                    elif nj == n:
                        nj = 0
                    d *= 10
                    d += a[ni][nj]
                ans = max(ans, d)
    print(ans)

di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]
