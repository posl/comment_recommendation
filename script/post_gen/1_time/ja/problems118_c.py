Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

N = int(input())
A = list(map(int, input().split()))

g = A[0]
for i in range(1, N):
    g = gcd(g, A[i])
print(g)

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans = math.gcd(ans, A[i])
    print(ans)

=======
Suggestion 5

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(max(A))
        return
    A.sort()
    ans = A[0]
    for i in range(1,N):
        ans = gcd(ans, A[i])
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(gcd_list(A))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 体力の最小値を出力する
    print(gcd_list(A))
