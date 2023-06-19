Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    print('{:.3f}'.format(b/a))
    return 0

=======
Suggestion 2

def main():
    a,b = map(int, input().split())
    print("{0:0.3f}".format(b/a))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print('{:.3f}'.format(b / a))

=======
Suggestion 4

def average_hit(a,b):
    s = round((b/a),3)
    return s

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    print("{:.3f}".format(b/a))

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print('{:.3f}'.format(b / a))

main()

=======
Suggestion 7

def get_input():
    a, b = [int(i) for i in input().split()]
    return a, b

=======
Suggestion 8

def get_result(a, b):
    return round(b/a, 3)

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    print('{:0.3f}'.format(b/a))
