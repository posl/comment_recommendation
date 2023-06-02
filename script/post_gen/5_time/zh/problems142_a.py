Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    print((n+1)//2/n)

=======
Suggestion 2

def main():
    N = int(input())
    print((N//2)/N)

=======
Suggestion 3

def main():
    n = int(input())
    if n == 1:
        print(1)
    else:
        print((n//2)/n)
main()

=======
Suggestion 4

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if i % 2 == 1:
            count += 1
    print('{:.10f}'.format(count/N))
