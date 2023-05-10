Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 1回目の切り込み時の角度
    theta = a[0]

    # 2回目以降の切り込み時の角度
    for i in range(1, n):
        theta += a[i]

    # 最大の角度を求める
    max_theta = 0
    for i in range(n):
        # 1回目の切り込み時の角度
        theta = a[i]

        # 2回目以降の切り込み時の角度
        for j in range(n):
            if i == j:
                continue
            theta += a[j]

        # 最大の角度を求める
        if theta > max_theta:
            max_theta = theta

    # 出力
    print(max_theta)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        tmp = 0
        for j in range(n):
            if i == j:
                continue
            tmp += a[j]
        ans = max(ans, min(tmp, 360-tmp))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    A.append(A[0])
    max_angle = 0
    for i in range(N):
        angle = A[i] - A[i+1]
        if angle < 0:
            angle += 360
        if angle > max_angle:
            max_angle = angle
    print(max_angle)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    a.append(a[0])
    max = 0

    for i in range(n):
        if max < (a[i] - a[i+1] + 360) % 360:
            max = (a[i] - a[i+1] + 360) % 360

    print(max)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += a[i]
        else:
            sum -= a[i]
    print(sum)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)

    max_angle = 0
    for i in range(N):
        angle = A[i]
        for j in range(i+1, N):
            angle += A[j]
            if angle >= 360:
                angle = angle % 360
        if max_angle < angle:
            max_angle = angle
        #print(i, angle)
    print(360 - max_angle)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    max = 0
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += A[(i+j)%N]
            if sum > max:
                max = sum
    print(max)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
    ans = 360 * N - ans
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = [a%360 for a in A]
    A.sort(reverse=True)
    A.append(A[0]+360)
    ans = 0
    for i in range(N):
        ans = max(ans, A[i]-A[i+1])
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print("N:", N)
    #print("A:", A)
    #print("A[0]:", A[0])
    #print("A[1]:", A[1])
    #print("A[2]:", A[2])
    #print("A[3]:", A[3])
    #print("A[4]:", A[4])
    #print("A[5]:", A[5])
    #print("A[6]:", A[6])
    #print("A[7]:", A[7])
    #print("A[8]:", A[8])
    #print("A[9]:", A[9])
    #print("A[10]:", A[10])
    #print("A[11]:", A[11])
    #print("A[12]:", A[12])
    #print("A[13]:", A[13])
    #print("A[14]:", A[14])
    #print("A[15]:", A[15])
    #print("A[16]:", A[16])
    #print("A[17]:", A[17])
    #print("A[18]:", A[18])
    #print("A[19]:", A[19])
    #print("A[20]:", A[20])
    #print("A[21]:", A[21])
    #print("A[22]:", A[22])
    #print("A[23]:", A[23])
    #print("A[24]:", A[24])
    #print("A[25]:", A[25])
    #print("A[26]:", A[26])
    #print("A[27]:", A[27])
    #print("A[28]:", A[28])
    #print("A[29]:", A[29])
    #print("A[30]:", A[30])
    #print("A[31]:", A[31])
    #print("A[32]:", A[32])
    #print("A[33]:", A[33])
    #print("A[34]:", A[34])
    #print("A[35]:", A
