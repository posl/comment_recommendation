Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_intrinsic_evaluation(n,r):
    if n >= 10:
        return r
    else:
        return r + 100 * (10 - n)

=======
Suggestion 2

def get_inner_grade(n, r):
    if n < 10:
        return r + 100 * (10 - n)
    else:
        return r

=======
Suggestion 3

def main():
    n,r = map(int,input().split())
    if n >= 10:
        print(r)
    else:
        print(r+100*(10-n))

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def get_inner_score(n, r):
    return r + 100 * max(10 - n, 0)

=======
Suggestion 6

def getInnerScore(n,r):
    if n >= 10:
        return r
    else:
        return r + (10-n)*100
