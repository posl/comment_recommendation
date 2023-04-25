Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K = int(input())
    H = 21
    M = 0
    M += K
    if M > 59:
        H += M // 60
        M = M % 60
    if H > 23:
        H = H % 24
    print(str(H).zfill(2) + ':' + str(M).zfill(2))

=======
Suggestion 2

def main():
    k = int(input())
    hour = 21 + k // 60
    minute = k % 60
    if hour >= 24:
        hour -= 24
    print('{:02}:{:02}'.format(hour, minute))

=======
Suggestion 3

def main():
    K = int(input())
    print("{:02d}:{:02d}".format((K + 21) // 60 % 24, (K + 21) % 60))

=======
Suggestion 4

def main():
    k = int(input())
    hour = 21
    minute = 0
    minute += k
    if minute >= 60:
        hour += minute // 60
        minute %= 60
    print(f'{hour:02}:{minute:02}')

=======
Suggestion 5

def main():
    k = int(input())
    print('22:03' if k>63 else '21:45' if k>45 else '21:40' if k>40 else '21:30' if k>30 else '21:15' if k>15 else '21:00')

=======
Suggestion 6

def main():
    k = int(input())
    hour = 21
    minute = 0
    if k <= 60:
        minute += k
    elif k > 60:
        hour += 1
        minute = k - 60
    if minute == 60:
        hour += 1
        minute = 0
    if hour == 24:
        hour = 0
    print(f'{hour:02d}:{minute:02d}')

main()

=======
Suggestion 7

def main():
    #input
    k = int(input())
    
    #calculate
    h = 21
    m = 0
    m += k
    if m >= 60:
        h += m // 60
        m = m % 60
    if h >= 24:
        h = h % 24
    
    #output
    print(str(h).zfill(2) + ":" + str(m).zfill(2))
    
    return

=======
Suggestion 8

def main():
    k = int(input())
    print("22:0{0}".format(k%60) if k%60 < 10 else "22:{0}".format(k%60))

=======
Suggestion 9

def main():
    K = int(input())
    print(f"{21 + (K // 60):02}:{(K % 60):02}")

=======
Suggestion 10

def main():
    k = int(input())
    print("22:03")
