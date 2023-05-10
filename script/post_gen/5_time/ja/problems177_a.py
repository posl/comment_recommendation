Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def check():
    D, T, S = input().split()
    D = int(D)
    T = int(T)
    S = int(S)
    if D <= T * S:
        print("Yes")
    else:
        print("No")

check()

=======
Suggestion 2

def main():
    d, t, s = map(int, input().split())
    if d <= t * s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    D, T, S = map(int, input().split())
    if D > T * S:
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def check(D, T, S):
    if D / S <= T:
        return True
    else:
        return False

=======
Suggestion 5

def main():
    d,t,s = map(int, input().split())
    if d/s <= t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def wait_meeting_place(D,T,S):
    if D / S <= T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    D, T, S = map(int, input().split())
    if T*S >= D:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def check():
    #input
    D, T, S = map(int, input().split())
    #calc
    if D/S <= T:
        print('Yes')
    else:
        print('No')
