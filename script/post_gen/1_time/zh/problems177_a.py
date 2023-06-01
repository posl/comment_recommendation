Synthesizing 10/10 solutions

=======
Suggestion 1

def is_on_time(D,T,S):
    if D/S <= T:
        return True
    else:
        return False

=======
Suggestion 2

def problem177_a():
    d,t,s = map(int, raw_input().split())
    if d <= s*t:
        print "Yes"
    else:
        print "No"
problem177_a()

=======
Suggestion 3

def problem177_a():
    d,t,s = map(int,input().split())
    if d <= t*s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def problem177_a():
    D, T, S = map(int, input().split())
    if D / S <= T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    d, t, s = map(int, input().split())
    print("Yes" if d <= t * s else "No")

=======
Suggestion 6

def problem177_a():
    # 输入
    D, T, S = map(int, input().split())

    # 处理
    if D / S <= T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    D, T, S = map(int, input().split())

    if D <= T * S:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    d,t,s = map(int, input().split())
    if d <= t*s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    d, t, s = (int(i) for i in input().split())
    if d <= t * s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    D,T,S = map(int,input().split())
    if D <= T*S:
        print("Yes")
    else:
        print("No")
