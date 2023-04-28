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
    # input
    A, B, C, D, E = map(int, input().split())

    # compute

    # output
    print(5-len(set([A, B, C, D, E]))+1)

=======
Suggestion 4

def main():
    a,b,c,d,e = map(int, input().split())
    list = [a,b,c,d,e]
    print(len(set(list)))

=======
Suggestion 5

def main():
    a,b,c,d,e = map(int,input().split())
    arr = [a,b,c,d,e]
    print(len(set(arr)))

=======
Suggestion 6

def main():
    a = input().split()
    b = list(set(a))
    print(len(b))
main()
