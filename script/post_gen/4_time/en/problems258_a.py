Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K = int(input())

    if K < 60:
        print('21:{:02d}'.format(K))
    elif K < 120:
        print('22:{:02d}'.format(K - 60))
    elif K < 180:
        print('23:{:02d}'.format(K - 120))
    elif K < 240:
        print('00:{:02d}'.format(K - 180))
    elif K < 300:
        print('01:{:02d}'.format(K - 240))
    elif K < 360:
        print('02:{:02d}'.format(K - 300))
    elif K < 420:
        print('03:{:02d}'.format(K - 360))
    elif K < 480:
        print('04:{:02d}'.format(K - 420))
    elif K < 540:
        print('05:{:02d}'.format(K - 480))
    elif K < 600:
        print('06:{:02d}'.format(K - 540))
    elif K < 660:
        print('07:{:02d}'.format(K - 600))
    elif K < 720:
        print('08:{:02d}'.format(K - 660))
    elif K < 780:
        print('09:{:02d}'.format(K - 720))
    elif K < 840:
        print('10:{:02d}'.format(K - 780))
    elif K < 900:
        print('11:{:02d}'.format(K - 840))
    elif K < 960:
        print('12:{:02d}'.format(K - 900))
    elif K < 1020:
        print('13:{:02d}'.format(K - 960))
    elif K < 1080:
        print('14:{:02d}'.format(K - 1020))
    elif K < 1140:
        print('15:{:02d}'.format(K - 1080))
    elif K < 1200:
        print('16:{:02d}'.format(K - 1140))
    elif K < 1260:
        print('17:{:02d}'.format(K - 1200))
    elif K < 1320:
        print('18:{:02d}'.format(K - 1260))

=======
Suggestion 2

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print("{:02}:{:02}".format(21+h,m))

=======
Suggestion 3

def main():
    k = int(input())
    h = 21
    m = 0
    if k <= 59:
        m = k
    else:
        h += k // 60
        m = k % 60
    print(str(h).zfill(2) + ":" + str(m).zfill(2))

=======
Suggestion 4

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print(f"{h+21:02}:{m:02}")

=======
Suggestion 5

def main():
    K = int(input())
    print('{:02d}:{:02d}'.format((K+2100)//100, (K+2100)%100))

=======
Suggestion 6

def main():
    # Take input Here and Call solution function
    K = int(input())
    print(solution(K))

=======
Suggestion 7

def main():
    K = int(input())
    print('%02d:%02d' % (21+K//60, K%60))

=======
Suggestion 8

def problem():
    K = int(input())
    print(21 + (K + 9) // 60, (K + 9) % 60, sep=':')

=======
Suggestion 9

def time_after_21(k):
    hour = 21 + int(k/60)
    minute = k%60
    if hour >= 24:
        hour = hour - 24
    if hour < 10:
        hour = '0' + str(hour)
    if minute < 10:
        minute = '0' + str(minute)
    return str(hour) + ':' + str(minute)

print(time_after_21(63))
print(time_after_21(45))
print(time_after_21(100))

=======
Suggestion 10

def solve(K: int):
    print('{:02d}:{:02d}'.format(*divmod((K + 21 * 60) % (24 * 60), 60)))
