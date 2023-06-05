Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l1 <= l2 and r1 >= r2:
        print(r2-l2)
    elif l1 >= l2 and r1 <= r2:
        print(r1-l1)
    elif l1 <= l2 and r1 <= r2 and r1 >= l2:
        print(r1-l2)
    elif l1 >= l2 and r1 >= r2 and r2 >= l1:
        print(r2-l1)
    else:
        print(0)

=======
Suggestion 2

def main():
    l1, r1, l2, r2 = map(int, input().split())
    if l1 <= l2 <= r1 <= r2:
        print(r1 - l2)
    elif l2 <= l1 <= r2 <= r1:
        print(r2 - l1)
    elif l1 <= l2 <= r2 <= r1:
        print(r2 - l2)
    elif l2 <= l1 <= r1 <= r2:
        print(r1 - l1)
    else:
        print(0)

=======
Suggestion 3

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l1 <= l2 and l2 < r1:
        if r1 <= r2:
            print(r1-l2)
        else:
            print(r2-l2)
    elif l2 <= l1 and l1 < r2:
        if r2 <= r1:
            print(r2-l1)
        else:
            print(r1-l1)
    else:
        print(0)

=======
Suggestion 4

def main():
    l1,r1,l2,r2=map(int,input().split())
    if r1<=l2 or r2<=l1:
        print(0)
    elif l1<=l2 and r2<=r1:
        print(r2-l2)
    elif l2<=l1 and r1<=r2:
        print(r1-l1)
    elif l1<=l2 and l2<=r1 and r1<=r2:
        print(r1-l2)
    elif l2<=l1 and l1<=r2 and r2<=r1:
        print(r2-l1)

=======
Suggestion 5

def main():
    l1,r1,l2,r2=map(int,input().split())
    print(max(0,min(r1,r2)-max(l1,l2)))

=======
Suggestion 6

def main():
    l1,r1,l2,r2 = map(int, input().split())
    l = max(l1,l2)
    r = min(r1,r2)
    print(max(r-l,0))

=======
Suggestion 7

def problems261_a():
    l1,r1,l2,r2 = map(int,input().split())
    if r1 <= l2 or r2 <= l1:
        print(0)
    elif l1 <= l2 and r1 <= r2:
        print(r1-l2)
    elif l2 <= l1 and r2 <= r1:
        print(r2-l1)
    elif l1 <= l2 and r1 <= r2:
        print(r1-l2)
    elif l2 <= l1 and r2 <= r1:
        print(r2-l1)

=======
Suggestion 8

def get_length(l1, r1, l2, r2):
    if l2 < l1 and r1 < r2:
        return r1 - l1
    elif l1 < l2 and r2 < r1:
        return r2 - l2
    elif l1 < l2 and l2 < r1 and r1 < r2:
        return r1 - l2
    elif l2 < l1 and l1 < r2 and r2 < r1:
        return r2 - l1
    else:
        return 0

=======
Suggestion 9

def main():
    l1,r1,l2,r2 = map(int,input().split())
    if l1 < l2:
        if r1 < l2:
            print(0)
        elif r1 < r2:
            print(r1 - l2)
        else:
            print(r2 - l2)
    else:
        if r2 < l1:
            print(0)
        elif r2 < r1:
            print(r2 - l1)
        else:
            print(r1 - l1)
