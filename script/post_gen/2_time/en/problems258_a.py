Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    h = 21
    m = 0
    while k > 0:
        m += 1
        if m == 60:
            m = 0
            h += 1
        k -= 1
    print(str(h).zfill(2) + ":" + str(m).zfill(2))

=======
Suggestion 2

def main():
    k = int(input())
    hour = k // 60
    minute = k % 60
    print(str(21 + hour).zfill(2) + ":" + str(minute).zfill(2))

=======
Suggestion 3

def main():
    K = int(input())
    H = K // 60
    M = K % 60
    print('{:02d}:{:02d}'.format(21+H, M))

=======
Suggestion 4

def main():
    K = int(input())
    print("{0:02d}:{1:02d}".format((K+2100)//100, (K+2100)%100))

=======
Suggestion 5

def main():
    k = int(input())
    print("{:02d}:{:02d}".format((2100+k)//100, (2100+k)%100))

=======
Suggestion 6

def main():
    k = int(input())
    print("{:02d}:{:02d}".format((k+120)//60, (k+120)%60))

=======
Suggestion 7

def main():
    K = int(input())
    hours = 21
    minutes = 0
    minutes += K % 60
    hours += int(K / 60)
    if minutes >= 60:
        minutes = minutes % 60
        hours += 1
    print(str(hours) + ":" + str(minutes).zfill(2))

=======
Suggestion 8

def abc258_a():
    k = int(input())
    print(21 + (k + 9) // 60, (k + 9) % 60, sep=':')

=======
Suggestion 9

def main():
    k = int(input())
    print("{:02d}:{:02d}".format((k+20)//60, (k+20)%60))
    return

=======
Suggestion 10

def main():
    min = int(input())
    hh = min // 60
    mm = min % 60
    print('{:02d}:{:02d}'.format(hh + 21, mm))
main()
