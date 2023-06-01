Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A,B = map(int, input().split())
    print('{:.3f}'.format(B/A))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    print("{:.3f}".format(b/a))

=======
Suggestion 3

def main():
    a,b = map(int,input().split())
    print("{:.3f}".format(b/a))
    return 0

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print('{:.3f}'.format(b/a))

=======
Suggestion 5

def calculate(A,B):
    result = B/A
    result = round(result,3)
    result = str(result)
    result = result+"000"
    return result[0:5]

A,B = input().split()
A = int(A)
B = int(B)
print(calculate(A,B))

=======
Suggestion 6

def problems274_a():
    a,b = input().split()
    a = int(a)
    b = int(b)
    print("{:0.3f}".format(b/a))
