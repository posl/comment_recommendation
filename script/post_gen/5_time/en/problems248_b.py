Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, k = map(int, input().split())
    count = 0
    while a < b:
        a *= k
        count += 1
    print(count)

=======
Suggestion 2

def main():
    A, B, K = map(int, input().split())
    count = 0
    while A < B:
        A *= K
        count += 1
    print(count)

=======
Suggestion 3

def solve():
    A, B, K = map(int, input().split())
    ans = 0
    while A < B:
        ans += 1
        A *= K
    print(ans)

=======
Suggestion 4

def count_shouts(a, b, k):
    count = 0
    while a < b:
        a = a * k
        count += 1
    return count

a, b, k = map(int, input().split())
print(count_shouts(a, b, k))

=======
Suggestion 5

def answer(A, B, K):
    count = 0
    while A < B:
        A *= K
        count += 1
    return count

=======
Suggestion 6

def problems248_b():
    a, b, k = map(int, input().split())
    count = 0
    while b // a > 0:
        a *= k
        count += 1
    print(count)

=======
Suggestion 7

def solve():
    a,b,k = map(int,input().split())
    ans = 0
    while a < b:
        ans += 1
        a *= k
    print(ans)

=======
Suggestion 8

def count_shout(A, B, K):
    if A >= B:
        return 0
    else:
        count = 1
        num = A * K
        while num < B:
            num = num * K
            count += 1
        return count

=======
Suggestion 9

def main():
    a,b,k = map(int,input().split())
    cnt=0
    while a < b:
        a*=k
        cnt+=1
    print(cnt)
