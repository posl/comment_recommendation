Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    D,T,S = map(int,input().split())
    if T*S>=D:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    d,t,s = map(int, input().split())
    if d/s <= t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    D,T,S = map(int,input().split())
    if D/S <= T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    d,t,s = map(int, input().split())
    if s*t >= d:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def can_meet(D,T,S):
    if D <= T*S:
        print('Yes')
    else:
        print('No')

can_meet(1000,15,80)
can_meet(2000,20,100)
can_meet(10000,1,1)

=======
Suggestion 6

def problem177_a():
    d, t, s = map(int, input().split())
    if d <= t * s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    D, T, S = map(int, raw_input().split())
    if D <= T * S:
        print "Yes"
    else:
        print "No"

main()

=======
Suggestion 8

def main():
    # 读取输入
    D, T, S = map(int, input().split())
    # 判断是否能准时到达
    if D / S <= T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def problem177_a():
    D, T, S = map(int, input().split())
    if D <= T * S:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    D, T, S = map(int, input().split())
    if D <= T * S:
        print('Yes')
    else:
        print('No')
