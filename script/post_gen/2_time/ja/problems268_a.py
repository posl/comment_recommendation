Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # input
    A, B, C, D, E = map(int, input().split())

    # compute

    # output
    print(len(set([A, B, C, D, E])))

=======
Suggestion 2

def main():
    a, b, c, d, e = map(int, input().split())
    print(len(set([a, b, c, d, e])))

=======
Suggestion 3

def main():
    a,b,c,d,e = map(int, input().split())
    if a != b and a != c and a != d and a != e and b != c and b != d and b != e and c != d and c != e and d != e:
        print(5)
    elif a == b and a == c and a == d and a == e and b == c and b == d and b == e and c == d and c == e and d == e:
        print(1)
    else:
        print(4)

=======
Suggestion 4

def main():
    a,b,c,d,e = map(int,input().split())
    l = [a,b,c,d,e]
    print(len(set(l)))

=======
Suggestion 5

def main():
    A,B,C,D,E = map(int,input().split())

    if A==B==C==D==E:
        print(1)
    else:
        print(5)

=======
Suggestion 6

def main():
    n = list(map(int, input().split()))
    print(len(set(n)))

=======
Suggestion 7

def main():
    num_list = input().split()
    num_set = set(num_list)
    print(len(num_set))

=======
Suggestion 8

def main():

    a = list(map(int, input().split()))
    print(len(set(a)))
