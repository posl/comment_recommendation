Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, H, M = map(int, input().split())
    h = (H + M / 60) * 30
    m = M * 6
    d = abs(h - m)
    if d > 180:
        d = 360 - d
    d = d / 180 * math.pi
    print(math.sqrt(A * A + B * B - 2 * A * B * math.cos(d)))

=======
Suggestion 2

def main():
    A, B, H, M = map(int, input().split())
    theta_h = 2 * math.pi * (H / 12 + M / 720)
    theta_m = 2 * math.pi * (M / 60)
    theta = abs(theta_h - theta_m)
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(theta)))

=======
Suggestion 3

def main():
    A, B, H, M = map(int, input().split())
    h = (H + M / 60) * 30
    m = M * 6
    rad = abs(h - m) * math.pi / 180
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(rad)))

=======
Suggestion 4

def main():
    A, B, H, M = map(int, input().split())
    theta = 2 * math.pi * (H/12 + M/720 - M/60)
    print(math.sqrt(A**2 + B**2 - 2*A*B*math.cos(theta)))

=======
Suggestion 5

def main():
    A, B, H, M = map(int, input().split())
    print(calc(A, B, H, M))

=======
Suggestion 6

def main():
    A, B, H, M = map(int, input().split())
    angle = abs(30*H-5.5*M)
    if angle > 180:
        angle = 360 - angle
    print((A**2+B**2-2*A*B*math.cos(math.radians(angle)))**0.5)

=======
Suggestion 7

def main():
    a,b,h,m = map(int, input().split())
    theta = 2 * math.pi * ((h + m / 60) / 12 - m / 60)
    print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(theta)))

=======
Suggestion 8

def solve():
    A, B, H, M = map(int, input().split())
    theta = (H*60+M)/720*2*math.pi
    phi = M/60*2*math.pi
    print(math.sqrt(A**2+B**2-2*A*B*math.cos(theta-phi)))

import math
solve()

=======
Suggestion 9

def  main():
     A ,  B ,  H ,  M  =  map( int ,  input().split())
     h  =  H  *   60   +  M
     m  =  M
     d1  =  ( h  -  m )  *   360   /   720 
     d2  =   360   -  d1
     d  =  min(d1, d2)

=======
Suggestion 10

def main():
    A,B,H,M = map(int,input().split())
    #print(A,B,H,M)
    #print(A**2+B**2)
    h = 30*H + M/2
    m = 6*M
    #print(h,m)
    if abs(h-m) > 180:
        if h > m:
            h,m = m,h
        m -= 360
    #print(h,m)
    print(((A**2+B**2-2*A*B*math.cos(math.radians(abs(h-m))))**0.5))
