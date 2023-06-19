Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[n//2]-d[n//2-1])

=======
Suggestion 2

def main():
    n = int(input())
    d = list(map(int,input().split()))
    d.sort()
    if n % 2 == 0:
        print(d[n//2] - d[n//2 - 1])
    else:
        print(0)

=======
Suggestion 3

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[N//2] - d[N//2-1])

main()

=======
Suggestion 4

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    # print(d)
    # print(d[N//2-1])
    # print(d[N//2])
    if d[N//2-1] == d[N//2]:
        print(0)
    else:
        print(d[N//2]-d[N//2-1])

=======
Suggestion 5

def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    n1 = n//2
    n2 = n1-1
    print(d[n1]-d[n2])

=======
Suggestion 6

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    #print(d)
    print(d[N//2] - d[N//2-1])

=======
Suggestion 7

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    print(d[N//2]-d[N//2-1])

=======
Suggestion 8

def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    k = d[n//2-1]
    print(d[n//2]-k)
