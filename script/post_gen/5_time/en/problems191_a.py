Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    V, T, S, D = map(int, input().split())
    if D / V >= T and D / V <= S:
        print("No")
    else:
        print("Yes")

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
    v, t, s, d = map(int, input().split())
    if d < v * t or v * s < d:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    v, t, s, d = map(int, input().split())
    if d/v < t or d/v > s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    v,t,s,d = map(int, input().split())
    if d < v*t or d > v*s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def problem191_a():
    v, t, s, d = map(int, input().split())
    if d < v * t or d > v * s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    v, t, s, d = map(int, input().split())
    print('Yes' if v*t <= d <= v*s else 'No')

=======
Suggestion 8

def main():
    v,t,s,d = map(int, input().split())
    if d/(v*t) <= s and d/(v*t) >= t:
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def main():
    V,T,S,D = map(int, input().split())
    print("Yes" if D < V*T or D > V*S else "No")

=======
Suggestion 10

def main():
    # Take input Here and Call solution function
    v,t,s,d = map(int,input().strip().split())
    solution(v,t,s,d)
