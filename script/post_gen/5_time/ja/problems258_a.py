Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    if h > 23:
        h = h - 24
    print('{0:02d}:{1:02d}'.format(h,m))

=======
Suggestion 2

def problems258_a():
    K = int(input())
    hour = K // 60
    minute = K % 60
    print("{:02d}:{:02d}".format(hour+21, minute))

=======
Suggestion 3

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print('{:02d}:{:02d}'.format((21+h)%24,m))

=======
Suggestion 4

def main():
    k = int(input())
    h = 21 + (k // 60)
    m = k % 60
    print('{0:02d}:{1:02d}'.format(h, m))

=======
Suggestion 5

def main():
    k = int(input())
    h = k // 60
    m = k - h * 60
    print("{0:02d}:{1:02d}".format(h + 21, m))
    return

=======
Suggestion 6

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print(str(21+h).zfill(2) + ":" + str(m).zfill(2))

=======
Suggestion 7

def main():
    K = int(input())
    H = K // 60
    M = K % 60
    print("{0:02d}:{1:02d}".format(H+21,M))

=======
Suggestion 8

def main():
    K = int(input())
    hour = K // 60
    minute = K % 60
    if hour > 23:
        hour = hour % 24
    print('{0:02d}:{1:02d}'.format(hour, minute))

=======
Suggestion 9

def main():
    k = int(input())
    h = int(k/60)
    m = k%60
    print(str(21+h).zfill(2)+":"+str(m).zfill(2))

=======
Suggestion 10

def main():
    k = int(input())
    h = 21
    m = 0
    m = m + (k % 60)
    h = h + (k // 60)
    if m >= 60:
        h = h + 1
        m = m - 60
    if h >= 24:
        h = h - 24
    if h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    print(str(h) + ":" + str(m))
