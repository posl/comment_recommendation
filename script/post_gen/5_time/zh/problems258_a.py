Synthesizing 10/10 solutions

=======
Suggestion 1

def problem258_a():
    k = int(input())
    h = 21
    m = 0
    for i in range(k):
        m += 1
        if m == 60:
            m = 0
            h += 1
    print('{:02}:{:02}'.format(h, m))

=======
Suggestion 2

def main():
    k = int(input())
    h = k//60
    m = k%60
    print('{:02d}:{:02d}'.format(h+21, m))

=======
Suggestion 3

def get_time(k):
    hour = 21
    minute = 0
    while k > 0:
        minute += 1
        if minute == 60:
            hour += 1
            minute = 0
        if hour == 24:
            hour = 0
        k -= 1
    return str(hour).zfill(2) + ':' + str(minute).zfill(2)

=======
Suggestion 4

def main():
    k = int(input())
    h = 21
    m = 0
    h += k // 60
    m += k % 60
    if m >= 60:
        h += 1
        m -= 60
    if h >= 24:
        h -= 24
    print("{:02d}:{:02d}".format(h, m))

=======
Suggestion 5

def f(k):
    m = k % 60
    h = k // 60 + 21
    if h > 23:
        h -= 24
    return '{:02d}:{:02d}'.format(h, m)

=======
Suggestion 6

def main():
    k = int(input())
    print("{:02d}:{:02d}".format((k+120)//60+21,(k+120)%60))

=======
Suggestion 7

def problem258_a():
    K = int(input())
    H = K // 60 + 21
    M = K % 60
    if M < 10:
        print(str(H) + ':0' + str(M))
    else:
        print(str(H) + ':' + str(M))

=======
Suggestion 8

def time_calculator(time):
    time = 21*60 + time
    hour = time // 60
    minute = time % 60
    return hour, minute

=======
Suggestion 9

def main():
    K = int(input())
    H = K // 60
    M = K % 60
    print("%02d:%02d" % (H + 21, M))

=======
Suggestion 10

def main():
    k = int(input())
    h = 21
    m = 0
    m = m + k
    if m >= 60:
        h = h + 1
        m = m - 60
    if m < 10:
        print(str(h) + ':0' + str(m))
    else:
        print(str(h) + ':' + str(m))
