Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    V, T, S, D = map(int, input().split())
    if V*T <= D <= V*S:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    v, t, s, d = map(int, input().split())
    if d < v * t or d > v * s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    V, T, S, D = map(int, input().split())
    if T*V <= D <= S*V:
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    V, T, S, D = map(int, input().split())
    if V*T <= D and D <= V*S:
        print('No')
    else:
        print('Yes')

=======
Suggestion 5

def main():
    v, t, s, d = map(int, input().split())
    if (d < v * t) or (d > v * s):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    v,t,s,d = map(int,input().split())
    if v*t <= d <= v*s:
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
  V,T,S,D = map(int,input().split())
  if D < V*T or D > V*S:
    print("Yes")
  else:
    print("No")

=======
Suggestion 8

def main():
    # Read input
    v, t, s, d = map(int, input().split())
    # Print output
    if d < v * t or v * s < d:
        print('Yes')
    else:
        print('No')
