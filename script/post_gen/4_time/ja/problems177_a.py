Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    D, T, S = map(int, input().split())
    if D / S <= T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    D, T, S = map(int, input().split())
    if D <= T * S:
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
    D, T, S = map(int, input().split())
    print("Yes" if D <= T * S else "No")

=======
Suggestion 5

def calc_time(d, s):
    return d / s
