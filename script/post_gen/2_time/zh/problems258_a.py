Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problems258_a():
    k = int(input())
    h = int(k / 60)
    m = k - h * 60
    print("%02d:%02d" % (h + 21, m))

=======
Suggestion 2

def main():
    k = int(input())
    h = 21
    m = 0
    if k >= 60:
        h = h + k // 60
        m = k % 60
    else:
        m = k
    if h >= 24:
        h = h - 24
    if h < 10:
        if m < 10:
            print("0" + str(h) + ":" + "0" + str(m))
        else:
            print("0" + str(h) + ":" + str(m))
    else:
        if m < 10:
            print(str(h) + ":" + "0" + str(m))
        else:
            print(str(h) + ":" + str(m))

=======
Suggestion 3

def main():
    K = int(input())
    hour = K // 60
    minute = K % 60
    print(f"{21 + hour:02}:{minute:02}")

=======
Suggestion 4

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print("{:02d}:{:02d}".format(21+h, m))

=======
Suggestion 5

def main():
    K = int(input())
    H = 21
    M = 0
    for i in range(K):
        M += 1
        if M == 60:
            M = 0
            H += 1
            if H == 24:
                H = 0
    if H < 10:
        print("0", end = "")
    print(H, end = ":")
    if M < 10:
        print("0", end = "")
    print(M)

=======
Suggestion 6

def main():
    k = int(input())
    hour = k // 60
    minute = k % 60
    if hour < 10:
        hour = '0'+str(hour)
    if minute < 10:
        minute = '0'+str(minute)
    print(str(21+hour)+':'+str(minute))

=======
Suggestion 7

def main():
    k = int(input())
    hour, minute = divmod(k, 60)
    hour = hour + 21
    minute = minute
    if hour > 23:
        hour = hour - 24
    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)
    print(hour + ":" + minute)

=======
Suggestion 8

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print("{0:02d}:{1:02d}".format(21+h%24,m))
    return

=======
Suggestion 9

def get_time(k):
    h = 21
    m = 0
    for i in range(k):
        m += 1
        if m == 60:
            m -= 60
            h += 1
            if h == 24:
                h -= 24
    return h, m
