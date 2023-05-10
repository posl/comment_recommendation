Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum([1 for x in a if x < P]))

=======
Suggestion 2

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] < p:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(len(list(filter(lambda x: x < p, a))))

=======
Suggestion 4

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(len([x for x in a if x < p]))

=======
Suggestion 5

def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if a[i] < P:
            count = count + 1
    print(count)

=======
Suggestion 6

def main():
    N,P=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    for i in range(N):
        if a[i]<P:
            ans+=1
    print(ans)

=======
Suggestion 7

def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if a[i] < p:
            cnt += 1
    print(cnt)
