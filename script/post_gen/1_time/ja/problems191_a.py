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
    V, T, S, D = map(int, input().split())
    if V*T <= D <= V*S:
        print('No')
    else:
        print('Yes')

=======
Suggestion 3

def main():
    V, T, S, D = map(int, input().split())
    if V*T <= D and D <= V*S:
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    V, T, S, D = map(int, input().split())
    if D < V * T or V * S < D:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def solve():
    V, T, S, D = map(int, input().split())
    if V * T <= D <= V * S:
        print("No")
    else:
        print("Yes")

=======
Suggestion 6

def main():
    v,t,s,d = map(int,input().split())
    if d >= v*t and d <= v*s:
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def main():
    v,t,s,d = map(int,input().split())
    if d/v >= t and d/v <= s:
        print('No')
    else:
        print('Yes')

=======
Suggestion 8

def main():
    #入力
    V,T,S,D = map(int,input().split())
    #出力
    if V*T <= D <= V*S:
        print("No")
    else:
        print("Yes")
