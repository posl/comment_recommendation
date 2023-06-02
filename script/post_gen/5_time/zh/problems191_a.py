Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    v,t,s,d = map(int,input().split())
    if d/v >= t and d/v <= s:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    v, t, s, d = map(int, input().split())
    if d >= v * t and d <= v * s:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    v,t,s,d = map(int, input().split())
    print("Yes" if d/v < t or d/v > s else "No")

=======
Suggestion 4

def judge():
    v,t,s,d = map(int, input().split())
    if d/v >= t and d/v <= s:
        print("No")
    else:
        print("Yes")

=======
Suggestion 5

def main():
    v, t, s, d = map(int, input().split())
    if d < v * t or d > v * s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    V,T,S,D = map(int,input().split())
    if (D/V) >= T and (D/V) <= S:
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
    V, T, S, D = map(int, input().split())
    print('No') if T * V <= D <= S * V else print('Yes')

=======
Suggestion 8

def main():
    V,T,S,D = map(int,input().split())
    if V*T <= D <= V*S:
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def problem191_a():
    v, t, s, d = map(int, input().split())
    if d < v * t or d > v * s:
        print("Yes")
    else:
        print("No")
