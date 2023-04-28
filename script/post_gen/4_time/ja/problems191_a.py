Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    v,t,s,d = map(int, input().split())
    if v*t <= d <= v*s:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    v, t, s, d = map(int, input().split())
    if d/v < t or d/v > s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    V,T,S,D = map(int,input().split())
    if D/V >= T and D/V <= S:
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    V,T,S,D = map(int,input().split())
    if D/V >= T and D/V <= S:
        print('No')
    else:
        print('Yes')

=======
Suggestion 5

def main():
    V,T,S,D = map(int,input().split())
    if V*T <= D and D <= V*S:
        print('No')
    else:
        print('Yes')

=======
Suggestion 6

def main():
    V,T,S,D = map(int,input().split())
    if D/V < T or D/V > S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    v, t, s, d = map(int, input().split())
    print("Yes" if d < v * t or d > v * s else "No")

=======
Suggestion 8

def solve():
    V,T,S,D = map(int,input().split())
    if D < V*T or D > V*S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    V, T, S, D = map(int, input().split())
    print("Yes" if D < V * T or D > V * S else "No")
    return
