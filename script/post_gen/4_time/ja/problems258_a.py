Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    h = 21
    m = 0
    while k > 0:
        m += 1
        k -= 1
        if m == 60:
            h += 1
            m = 0
        if h == 24:
            h = 0
    print('%02d:%02d' % (h, m))

=======
Suggestion 2

def main():
    K = int(input())
    H = K // 60
    M = K % 60
    print("{0:02d}:{1:02d}".format(H,M))

=======
Suggestion 3

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print("{:02d}:{:02d}".format(h+21 if h+21 < 24 else h+21-24, m))
    return

=======
Suggestion 4

def main():
    K = int(input())
    H = K // 60
    M = K % 60
    print("{0:02d}:{1:02d}".format(H+21, M))

=======
Suggestion 5

def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print("{:0>2}:{:0>2}".format(h + 21, m))

=======
Suggestion 6

def main():
    K = int(input())
    h = K // 60
    m = K % 60
    print(str(21+h).rjust(2,'0') + ':' + str(m).rjust(2,'0'))

=======
Suggestion 7

def main():
    k = int(input())
    h = 21
    m = 0
    if k < 60:
        m = k
    elif k >= 60:
        h = h + int(k / 60)
        m = k % 60
    print(str(h) + ':' + str(m).zfill(2))

=======
Suggestion 8

def main():
    #input
    k = int(input())
    #compute
    hour = k//60
    minute = k%60
    #output
    print("{0:02d}:{1:02d}".format(hour+21,minute))

=======
Suggestion 9

def main():
    k = int(input())
    k += 21 * 60
    print('{:0>2}:{:0>2}'.format(k//60%24,k%60))

=======
Suggestion 10

def main():
    import sys
    #input = sys.stdin.readline
    #print = sys.stdout.write
    #K = int(input())
    K = int(input())
    H = K // 60
    M = K % 60
    print("%02d:%02d" % (H,M))
