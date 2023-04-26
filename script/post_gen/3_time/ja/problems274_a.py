Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    print('{:.3f}'.format(B/A))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print("{:.3f}".format(round(b/a, 3)))

main()

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print("{:.3f}".format(b/a))
main()

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    print("{0:0.3f}".format(b/a))

=======
Suggestion 5

def main():
    A,B = map(int,input().split())
    print("{:0.3f}".format(B/A))

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(format(b/a,".3f"))

=======
Suggestion 7

def get_input():
    a, b = map(int, input().split())
    return a, b

=======
Suggestion 8

def func(a, b):
    return (b/a)

=======
Suggestion 9

def get_input_str():
    return input()
