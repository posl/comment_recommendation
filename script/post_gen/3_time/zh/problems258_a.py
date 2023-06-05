Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print("{:02d}:{:02d}".format(h + 21, m))

=======
Suggestion 2

def main():
    K = int(input())
    if K < 60:
        print("21:{}".format(60 + K))
    else:
        hour = 21 + (K // 60)
        minute = 60 + (K % 60)
        if minute >= 60:
            hour += 1
            minute -= 60
        print("{}:{}".format(hour, minute))

=======
Suggestion 3

def main():
    k = int(input())
    hour = k // 60
    minute = k % 60
    if hour < 10:
        hour = '0' + str(hour)
    if minute < 10:
        minute = '0' + str(minute)
    print(str(21 + hour) + ':' + str(minute))

=======
Suggestion 4

def main():
    k = int(input())
    print("{:02d}:{:02d}".format((k+120)//60+21,(k+120)%60))

=======
Suggestion 5

def main():
    K = int(input())
    H = K//60
    M = K%60
    print(str(21+H).zfill(2)+":"+str(M).zfill(2))

=======
Suggestion 6

def main():
    k = int(input())
    h = 21
    m = 0
    m += k
    while m >= 60:
        h += 1
        m -= 60
    if h >= 24:
        h -= 24
    if h < 10:
        h = '0' + str(h)
    if m < 10:
        m = '0' + str(m)
    print(str(h) + ':' + str(m))

=======
Suggestion 7

def main():
    K = int(input())
    hour = 21
    minute = 0
    for i in range(K):
        minute += 1
        if minute == 60:
            hour += 1
            minute = 0
        if hour == 24:
            hour = 0
    if hour < 10 and minute < 10:
        print('0' + str(hour) + ':' + '0' + str(minute))
    elif hour < 10:
        print('0' + str(hour) + ':' + str(minute))
    elif minute < 10:
        print(str(hour) + ':' + '0' + str(minute))
    else:
        print(str(hour) + ':' + str(minute))

=======
Suggestion 8

def problem258_a():
    k = int(input())
    h = k // 60
    m = k % 60
    print(f'{21 + h:02}:{m:02}')

=======
Suggestion 9

def main():
    k = int(input())
    h = 0
    m = 0
    if k >= 60:
        h = k // 60
        m = k % 60
    else:
        m = k
    print("%02d:%02d" % (h + 21, m))

=======
Suggestion 10

def main():
    k = int(input())
    h = k//60
    m = k%60
    print("{0:02d}:{1:02d}".format(h+21, m))
