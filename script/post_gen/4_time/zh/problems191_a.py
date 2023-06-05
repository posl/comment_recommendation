Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    v,t,s,d = map(int, input().split())
    if d >= v*t and d <= v*s:
        print('No')
    else:
        print('Yes')

=======
Suggestion 2

def main():
    v, t, s, d = map(int, input().split())

    if d / v >= t and d / v <= s:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    v,t,s,d = map(int, input().split())
    if (v * t <= d) and (d <= v * s):
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    v,t,s,d = map(int,input().split())
    if d/v < t or d/v > s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    v, t, s, d = map(int, input().split())
    # print(v, t, s, d)
    # print((d/v))
    if (d/v) >= t and (d/v) <= s:
        print("No")
    else:
        print("Yes")

=======
Suggestion 6

def main():
    v, t, s, d = map(int, input().split())
    if v*t <= d <= v*s:
        print('No')
    else:
        print('Yes')

=======
Suggestion 7

def main():
    v,t,s,d = map(int,input().split())
    if d < v*t or d > v*s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    v,t,s,d = map(int,input().split())
    if v*t <= d <= v*s:
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def problem191_a():
    v, t, s, d = map(int, input().split())
    if d / v >= t and d / v <= s:
        print('No')
    else:
        print('Yes')
