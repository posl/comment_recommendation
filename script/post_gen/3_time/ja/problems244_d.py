Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s1, s2, s3 = input().rstrip().split()
    t1, t2, t3 = input().rstrip().split()
    if s1 == t1 and s2 == t2 and s3 == t3:
        print("Yes")
    elif s1 == t1 and s2 == t3 and s3 == t2:
        print("Yes")
    elif s1 == t2 and s2 == t1 and s3 == t3:
        print("Yes")
    elif s1 == t2 and s2 == t3 and s3 == t1:
        print("Yes")
    elif s1 == t3 and s2 == t1 and s3 == t2:
        print("Yes")
    elif s1 == t3 and s2 == t2 and s3 == t1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    # input
    S = input()
    T = input()

    # compute

    # output
    if S == T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    S = input().split()
    T = input().split()
    if S == T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def get_input():
    s = input().split()
    t = input().split()
    return s, t
