Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, r = map(int, input().split())
    if n < 10:
        print(r + 100 * (10 - n))
    else:
        print(r)

=======
Suggestion 2

def main():
    N,R = map(int, input().split())
    if N >= 10:
        print(R)
    else:
        print(R + 100*(10-N))

=======
Suggestion 3

def main():
    n, r = map(int, input().split())
    if n >= 10:
        print(r)
    else:
        print(r + 100 * (10 - n))

=======
Suggestion 4

def main():
    n,r = map(int, input().strip().split())
    if n < 10:
        print(r + 100 * (10-n))
    else:
        print(r)

=======
Suggestion 5

def get_inner_score(outer_score, num_of_contest):
    if num_of_contest < 10:
        return outer_score + 100 * (10 - num_of_contest)
    else:
        return outer_score
