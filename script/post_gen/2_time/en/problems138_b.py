Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += 1/A[i]
    print(1/sum)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(1/sum(1/a for a in A))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(1/sum([1/a for a in A]))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum([1 / i for i in a]))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    sum = 0
    for i in range(N):
        sum += 1 / A[i]
    print(1 / sum)

=======
Suggestion 6

def main():
    #get input
    N = int(input())
    A = list(map(int, input().split()))
    
    #compute
    sum = 0
    for i in range(N):
        sum += 1 / A[i]
    ans = 1 / sum
    
    #print output
    print(ans)
