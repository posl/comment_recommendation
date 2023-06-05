Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += abs(a[i] - a[n//2])
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > ans:
            ans = A[i]
        elif A[i] < ans:
            print(-1)
            return
    print(ans)
main()

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    #print(N)
    #print(A)
    A.reverse()
    #print(A)
    res = 0
    for i in range(N):
        if A[i] > res:
            res = A[i]
        elif A[i] == res:
            res = A[i] - 1
        elif A[i] < res:
            res = A[i]
    print(res)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans += a[i]
        else:
            ans -= a[i]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # print(a)
    # print(n)
    # a = [2, 1, 5, 4, 3]
    # n = 5
    ans = 0
    for i in range(n):
        if a[i] > ans:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.reverse()
    max_height = 0
    for a in a_list:
        if a >= max_height:
            max_height = a
        else:
            max_height = a + max_height % a
    print(max_height)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(len(A))
    #print(A[2])
    #print(A[1])
    #print(A[0])
    #print(A[2] >= A[1])
    #print(A[1] >= A[0])
    #print(A[2] >= A[0])
    #print(A[3] >= A[2])
    #print(A[4] >= A[3])
    #print(A[4] >= A[2])
    #print(A[3] >= A[1])
    #print(A[2] >= A[0])
    #print(A[1] >= A[0])
    #print(A[4] >= A[3])
    #print(A[3] >= A[2])
    #print(A[2] >= A[1])
    #print(A[1] >= A[0])
    #print(A[4] >= A[2])
    #print(A[3] >= A[1])
    #print(A[2] >= A[0])
    #print(A[4] >= A[1])
    #print(A[3] >= A[0])
    #print(A[4] >= A[0])
    #print(A[0] >= A[0])
    #print(A[1] >= A[1])
    #print(A[2] >= A[2])
    #print(A[3] >= A[3])
    #print(A[4] >= A[4])
    #print(A[0] >= A[1])
    #print(A[0] >= A[2])
    #print(A[0] >= A[3])
    #print(A[0] >= A[4])
    #print(A[1] >= A[2])
    #print(A[1] >= A[3])
    #print(A[1] >= A[4])
    #print(A[2] >= A[3])
    #print(A[2] >= A[4])
    #print(A[3] >= A[4])
    #print(A[0] >= A[0])
    #print(A[1] >= A[1])
    #print(A[2] >= A[2])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(len(a)):
        if a[i] > count:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    b.append(0)
    for i in range(n):
        b.append(a[i])
    b.append(0)
    sum = 0
    for i in range(n+1):
        sum += abs(b[i+1]-b[i])
    sum += abs(b[n+1])
    for i in range(n):
        print(sum-abs(b[i+1]-b[i])-abs(b[i+2]-b[i+1])+abs(b[i+2]-b[i]))
    print(sum-abs(b[n+1]-b[n])-abs(b[n]-b[n-1])+abs(b[n+1]-b[n-1]))

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(n):
        if a[i] <= max:
            count += max - a[i]
        else:
            max = a[i]
    print(count)
