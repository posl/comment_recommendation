Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(n, lines):
    """
    :param n: the number of lines
    :param lines: the length and speed of each line
    :return: the distance of the two flames
    """

=======
Suggestion 2

def problems223_c():
    return None

=======
Suggestion 3

def calc_distance(a, b, c, d):
    return (a * c + b * d) / (b + d)

=======
Suggestion 4

def solve():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        ans += ab[i][0] / ab[i][1]
    ans /= 2
    ans2 = 0
    for i in range(n):
        ans2 += ab[i][0]
        if ans2 >= ans:
            ans2 -= ab[i][0]
            ans2 += (ans - ans2) * ab[i][1]
            break
    print(ans2)

solve()

=======
Suggestion 5

def solve():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int,input().split())))
    #print(AB)
    #print(N)
    #print(AB[0][0])
    #print(AB[0][1])
    #print(AB[1][0])
    #print(AB[1][1])
    #print(AB[2][0])
    #print(AB[2][1])
    #print(AB[3][0])
    #print(AB[3][1])
    #print(AB[4][0])
    #print(AB[4][1])
    #print(AB[5][0])
    #print(AB[5][1])
    #print(AB[6][0])
    #print(AB[6][1])
    #print(AB[7][0])
    #print(AB[7][1])
    #print(AB[8][0])
    #print(AB[8][1])
    #print(AB[9][0])
    #print(AB[9][1])
    #print(AB[10][0])
    #print(AB[10][1])
    #print(AB[11][0])
    #print(AB[11][1])
    #print(AB[12][0])
    #print(AB[12][1])
    #print(AB[13][0])
    #print(AB[13][1])
    #print(AB[14][0])
    #print(AB[14][1])
    #print(AB[15][0])
    #print(AB[15][1])
    #print(AB[16][0])
    #print(AB[16][1])
    #print(AB[17][0])
    #print(AB[17][1])
    #print(AB[18][0])
    #print(AB[18][1])
    #print(AB[19][0])
    #print(AB[19][1])
    #print(AB[20][0])
    #print(AB[20][1])
    #print(AB[21][0])
    #print(AB[21][1])
    #print(AB[22][0])
    #print(AB[22][1])

=======
Suggestion 6

def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split(' '))))
    left = 0
    right = 0
    for i in range(n):
        left = left + ab[i][0] / ab[i][1]
    for i in range(n - 1, -1, -1):
        right = right + ab[i][0] / ab[i][1]
    print(left / 2 + right / 2)

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    sum = 0
    for i in range(N):
        sum += A[i]/B[i]
    sum /= 2
    sum2 = 0
    for i in range(N):
        sum2 += A[i]
        if sum2 >= sum:
            print(sum2 - (sum2 - A[i]) / B[i])
            break

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 从左端开始燃烧
    left = 0
    for i in range(N):
        left += A[i] / B[i]

    # 从右端开始燃烧
    right = 0
    for i in range(N):
        right += A[N - i - 1] / B[N - i - 1]

    # 火焰相遇的位置
    meet = 0
    for i in range(N):
        meet += A[i] / B[i] * 0.5

    print(left - meet)
    print(right - meet)

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
    left = 0
    right = sum(A)
    while right - left > 10**(-6):
        mid = (right + left) / 2
        t = 0
        for i in range(N):
            t += A[i] / (B[i] + mid)
        if t > mid:
            left = mid
        else:
            right = mid
    print(left)
