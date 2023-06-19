Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = input().split()
    a = int(a)
    b = float(b)
    c = a*b
    print(int(c))
main()

=======
Suggestion 2

def main():
    a,b=map(float,input().split())
    print(int(a*b))

=======
Suggestion 3

def main():
    a,b = input().split()
    a = int(a)
    b = float(b)
    print(int(a*b))

=======
Suggestion 4

def main():
    A,B = map(float,input().split())
    print(int(A * B))

=======
Suggestion 5

def main():
    a,b = map(float, input().split())
    print(int(a*b))
    return

=======
Suggestion 6

def main():
    a, b = input().split()
    a = int(a)
    b = int(b.replace('.', ''))
    print(a * b // 100)
