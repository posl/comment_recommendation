Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K = int(input())
    H = K // 60
    M = K % 60
    print("{0:02d}:{1:02d}".format(21 + H % 24, M))

=======
Suggestion 2

def main():
    K = int(input())
    #print(K)
    H = K // 60
    #print(H)
    M = K % 60
    #print(M)
    if H < 10:
        H = "0" + str(H)
    if M < 10:
        M = "0" + str(M)
    print(str(21 + int(H)) + ":" + str(M))

=======
Suggestion 3

def format_time(time):
    if time < 10:
        return '0' + str(time)
    else:
        return str(time)

=======
Suggestion 4

def main():
    k = int(input())
    h = 21
    m = 0
    for i in range(k):
        if m == 59:
            h += 1
            m = 0
        else:
            m += 1
    if h < 10:
        h = "0" + str(h)
    else:
        h = str(h)
    if m < 10:
        m = "0" + str(m)
    else:
        m = str(m)
    print(h + ":" + m)

=======
Suggestion 5

def problem258_a():
    import sys
    # 读取输入
    K = int(sys.stdin.readline().strip())
    # 计算
    hour = 21 + (K // 60)
    min = K % 60
    # 输出
    print(str(hour).zfill(2) + ":" + str(min).zfill(2))

=======
Suggestion 6

def main():
    k = int(input())
    h = 21
    m = 0
    for i in range(k):
        m += 1
        if m == 60:
            m = 0
            h += 1
    print(str(h).zfill(2) + ':' + str(m).zfill(2))

=======
Suggestion 7

def main():
    k = int(input())
    hour = 21 + k // 60
    minute = k % 60
    print(f'{hour:02d}:{minute:02d}')

=======
Suggestion 8

def print_time(k):
    hour = 21
    minute = 0
    if k < 60:
        minute = minute + k
    else:
        hour = hour + int(k / 60)
        minute = minute + k % 60
    if minute >= 60:
        hour = hour + 1
        minute = minute - 60
    if hour >= 24:
        hour = hour - 24
    print(str(hour).zfill(2) + ':' + str(minute).zfill(2))

=======
Suggestion 9

def problems258_a():
    K = int(input())
    h = K // 60
    m = K % 60
    print("{0:02d}:{1:02d}".format(21+h,m))

=======
Suggestion 10

def main():
    k = int(input())
    h = k // 60
    m = k - h * 60
    print("{:02d}:{:02d}".format(h + 21, m))
