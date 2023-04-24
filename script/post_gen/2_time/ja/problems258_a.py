Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    if h >= 24:
        h = h % 24
    print('{:02d}:{:02d}'.format(h, m))

=======
Suggestion 2

def main():
    k = int(input())
    h = 21
    m = 0
    while k > 0:
        if m == 60:
            h += 1
            m = 0
        k -= 1
        m += 1
    print(str(h).zfill(2) + ":" + str(m).zfill(2))

=======
Suggestion 3

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print("{:02d}:{:02d}".format(h,m))

=======
Suggestion 4

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print("{:02}:{:02}".format(h + 21, m))

=======
Suggestion 5

def main():
    K = int(input())
    h = K // 60
    m = K % 60
    print("{0:02d}:{1:02d}".format(h+21,m))

=======
Suggestion 6

def main():
    k = int(input())
    hh = 21 + k // 60
    mm = k % 60
    print("{:02}:{:02}".format(hh, mm))

=======
Suggestion 7

def main():
    K = int(input())
    H = K // 60
    M = K % 60
    print('{:02d}:{:02d}'.format(H+21, M))

=======
Suggestion 8

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print('{:0=2}:{:0=2}'.format(21+h%24, m))

=======
Suggestion 9

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print('{:02}:{:02}'.format(21+h, m))

=======
Suggestion 10

def main():
    k = int(input())
    print("{:02d}:{:02d}".format((k+20)//60, (k+20)%60))
