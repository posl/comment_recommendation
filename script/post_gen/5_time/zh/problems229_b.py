Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    if len(str(a+b)) > len(str(a)) or len(str(a+b)) > len(str(b)):
        print("Hard")
    else:
        print("Easy")
main()

=======
Suggestion 2

def problems229_b():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a+b >= 10**18:
        print('Hard')
    else:
        print('Easy')

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a + b >= 10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    if a+b >= 10**10:
        print('Hard')
    else:
        print('Easy')
    return

=======
Suggestion 5

def main():
    A,B = map(int, input().split())
    if A+B < 10:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    if a+b < 10:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 7

def main():
    # input
    a,b = map(int,input().split())
    # process
    if a+b < 10:
        print("Easy")
    else:
        print("Hard")
    # output

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    if A + B >= 10 ** 10:
        print("Hard")
    else:
        print("Easy")
