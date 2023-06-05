Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A,B = input().split()
    A = int(A)
    B = float(B)
    print(int(A*B))

=======
Suggestion 2

def main():
    a,b = map(float,input().split())
    print(int(a*b))

=======
Suggestion 3

def main():
    a, b = input().split()
    a = int(a)
    b = float(b)
    print(int(a*b))

=======
Suggestion 4

def main():
    a,b = input().split()
    a = int(a)
    b = float(b)
    print(int(a*b))
    
main()

=======
Suggestion 5

def main():
    num = input().split()
    a = int(num[0])
    b = float(num[1])
    print(int(a * b))

=======
Suggestion 6

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return int(stepper * number) / stepper
