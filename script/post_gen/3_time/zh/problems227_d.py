Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(sum(a[:k]))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(a)
    print(a[-k:])

    ans = 0
    for i in a[-k:]:
        ans += i
    print(ans)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    #print(a)
    #print(n,k)
    #print(a)
    #print(a[0])
    #print(a[n-1])
    #print(a[0]*a[n-1])
    if k == 1:
        print(a[0]*a[n-1])
        return
    elif k == n:
        print(1)
        return
    else:
        if a[0] == a[n-1]:
            print(1)
            return
        else:
            if a[0] == 1:
                print(1)
                return
            else:
                for i in range(2,a[0]+1):
                    #print(i)
                    if a[0]%i == 0 and a[n-1]%i == 0:
                        print(i)
                        return
                print(1)
                return
    print(1)
    return

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = []
    for i in range(n-1):
        b.append(a[i+1]-a[i])
    b.sort()
    print(sum(b[0:n-k]))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    l = 0
    r = N - 1
    ans = 0
    while l <= r:
        if A[l] + A[r] >= K:
            ans += 1
            r -= 1
        l += 1
    print(ans)

=======
Suggestion 6

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    #print(len(a))
    #print(a[0])
    #print(a[len(a)-1])
    #print(a[len(a)-1]-a[0])
    #print(k)
    #print(n)
    if k == 1:
        print(n)
    elif k == n:
        print(1)
    else:
        print(n-k+1)

=======
Suggestion 7

def input():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    return n,k,a

=======
Suggestion 8

def problems227_d():
    pass

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    count = 0
    for i in range(k):
        count += a[i]
    print(count)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    b = [0] * n
    for i in range(n):
        b[a[i]-1] += 1

    ans = 0
    for i in range(n):
        if b[i] >= k:
            ans += 1

    print(ans)
