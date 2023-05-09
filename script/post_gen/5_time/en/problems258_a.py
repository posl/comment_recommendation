Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print("{:02d}:{:02d}".format(21 + h % 24, m))

=======
Suggestion 2

def main():
    K = int(input())
    H = K // 60
    M = K % 60
    print('{:02}:{:02}'.format(H + 21, M))

=======
Suggestion 3

def main():
    K = int(input())
    hour = 21
    minute = 0
    minute += K
    if minute >= 60:
        minute -= 60
        hour += 1
    print(str(hour).zfill(2) + ":" + str(minute).zfill(2))

=======
Suggestion 4

def main():
    k = int(input())
    print(str(21+(k//60)).zfill(2)+":"+str(k%60).zfill(2))

=======
Suggestion 5

def main():
    K = int(input())
    print("{:02}:{:02}".format((K+2100)//100, (K+2100)%100))

=======
Suggestion 6

def main():
    K = int(input())
    print('{:02d}:{:02d}'.format((K+120)//60, (K+120)%60))

=======
Suggestion 7

def main():
    K = int(input())
    print("{:02d}:{:02d}".format((K//60+21)%24,K%60))

=======
Suggestion 8

def main():
    k = int(input())
    time = 2100
    hour = k // 60
    minute = k % 60
    time = time + hour * 100 + minute
    print("{:04d}".format(time))

=======
Suggestion 9

def main():
    k = int(input())
    print(f"{21 + k // 60:02}:{k % 60:02}")

=======
Suggestion 10

def get_time(k):
    # 21:00 JST
    hour = 21
    minute = 0

    # 100 minutes
    minute += k

    # 60 minutes = 1 hour
    hour += minute // 60
    minute = minute % 60

    # 24 hours = 1 day
    hour = hour % 24

    # 1 digit to 2 digits
    hour_str = str(hour)
    minute_str = str(minute)
    if len(hour_str) == 1:
        hour_str = '0' + hour_str
    if len(minute_str) == 1:
        minute_str = '0' + minute_str

    return hour_str + ':' + minute_str
