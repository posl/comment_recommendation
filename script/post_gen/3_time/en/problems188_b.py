Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum([a[i] * b[i] for i in range(n)]) == 0:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum([a[i]*b[i] for i in range(n)]) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if sum([A[i]*B[i] for i in range(N)]) == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if sum([A[i]*B[i] for i in range(N)]) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print("Yes" if sum([A[i] * B[i] for i in range(N)]) == 0 else "No")

main()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if sum([a*b for a,b in zip(A,B)]) == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print("Yes" if sum([a[i]*b[i] for i in range(n)]) == 0 else "No")

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    dot = 0
    for i in range(N):
        dot += A[i] * B[i]
    if dot == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    #compute
    ab = 0
    for i in range(N):
        ab += A[i] * B[i]

    #output
    if ab == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    #input
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    #calc
    ans = 0
    for i in range(N):
        ans += A[i]*B[i]
    
    #output
    if ans == 0:
        print("Yes")
    else:
        print("No")
