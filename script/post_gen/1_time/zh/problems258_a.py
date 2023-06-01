Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K = int(input())
    H = K//60
    M = K%60
    print("{:02}:{:02}".format(H+21,M))

=======
Suggestion 2

def time(k):
    h = k//60
    m = k%60
    if h<10:
        h = '0'+str(h)
    else:
        h = str(h)
    if m<10:
        m = '0'+str(m)
    else:
        m = str(m)
    return h+':'+m
k = int(input())
print(time(k))

=======
Suggestion 3

def print_time(k):
    start_time = 21 * 60
    end_time = start_time + 100
    k_time = start_time + k
    if k_time < end_time:
        hour = k_time // 60
        minute = k_time % 60
        print("%02d:%02d" % (hour, minute))
    else:
        print("00:00")

=======
Suggestion 4

def main():
    # 读取输入
    k = int(input())

    # 计算结果
    h = k // 60
    m = k % 60

    # 输出
    print("{:02d}:{:02d}".format(h+21, m))

=======
Suggestion 5

def main():
    # input
    K = int(input())

    # solve
    hour = 21
    minute = 0
    for i in range(K):
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
        if hour == 24:
            hour = 0

    # output
    print("{:02d}:{:02d}".format(hour, minute))

=======
Suggestion 6

def main():
    K = int(input())
    H = 21
    M = 0
    if K >= 60:
        H += K // 60
        M = K % 60
    else:
        M = K
    if H >= 24:
        H = H % 24
    if H < 10:
        if M < 10:
            print("0%d:0%d" % (H, M))
        else:
            print("0%d:%d" % (H, M))
    else:
        if M < 10:
            print("%d:0%d" % (H, M))
        else:
            print("%d:%d" % (H, M))

=======
Suggestion 7

def problem258_a():
    k = int(input())
    h = k//60
    m = k%60
    print("{:02d}:{:02d}".format(21+h,m))

=======
Suggestion 8

def print_time(k):
    hour = 21 + int(k / 60)
    minute = k % 60
    if hour > 23:
        hour = hour - 24
    if hour < 10:
        hour = "0" + str(hour)
    if minute < 10:
        minute = "0" + str(minute)
    print(str(hour) + ":" + str(minute))

=======
Suggestion 9

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print("{:02d}:{:02d}".format(h + 21, m))

=======
Suggestion 10

def time_calculator(k):
    if k == 0:
        return "21:00"
    else:
        hour = 21
        minute = 0
        for i in range(k):
            minute += 1
            if minute == 60:
                hour += 1
                minute = 0
            if hour == 24:
                hour = 0
        if hour < 10:
            hour = "0" + str(hour)
        else:
            hour = str(hour)
        if minute < 10:
            minute = "0" + str(minute)
        else:
            minute = str(minute)
        return hour + ":" + minute
