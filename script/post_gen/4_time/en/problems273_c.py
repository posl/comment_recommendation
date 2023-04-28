Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0]*n
    for i in range(n-1):
        if a[i] != a[i+1]:
            ans[i] = 1
    ans[n-1] = 1
    for i in range(n-1, 0, -1):
        if a[i-1] != a[i]:
            ans[i] += ans[i-1]
    for i in range(n):
        print(n-ans[i])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(-1)
    ans = [0] * n
    cnt = 1
    for i in range(n):
        if a[i] == a[i+1]:
            cnt += 1
        else:
            ans[cnt-1] += 1
            cnt = 1
    for i in range(n):
        print(ans[i])
main()

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    ans = [0] * n
    ans[0] = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            ans[i] = ans[i - 1] + 1
        else:
            ans[i] = ans[i - 1]
    for i in range(n):
        print(ans[a.index(a[i])] - 1)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0 for i in range(N)]
    for i in range(N):
        ans[i] = A.count(A[i]) - 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = list

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    ans = [0 for i in range(N)]
    count = 1
    for i in range(N):
        if A[i] != A[i+1]:
            ans[count-1] += 1
            count = 1
        else:
            count += 1
    print('\n'.join(map(str, ans)))

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    prev = 0
    ans = [0] * n
    for i in range(n):
        if i == 0 or a[i] != prev:
            prev = a[i]
            ans[i] = 1
        else:
            ans[i] = ans[i-1] + 1
    for i in range(n):
        print(n - ans[-1 - i])

=======
Suggestion 8

def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = sorted(a)
    c = [0] * n
    for i in range(n):
        c[b[i]] = i
    ans = [0] * n
    for i in range(n):
        ans[i] = c[a[i]]
    print(*ans, sep='\n')

solve()

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(-1)

    ret = [0] * N
    cnt = 1
    for i in range(N):
        if A[i] != A[i+1]:
            ret[cnt-1] += 1
            cnt = 1
        else:
            cnt += 1

    print('\n'.join(map(str, ret)))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    A.sort()
    #print(A)
    #print(len(A))
    #print(len(set(A)))
    #print(A)
    #print(set(A))
    #print(len(set(A))-1)
    #print(len(A)-1)
    #print(len(A)-len(set(A)))
    #print(len(A)-len(set(A))-1)
    #print(len(A)-len(set(A))+1)
    #print(len(A)-len(set(A))+2)
    #print(len(A)-len(set(A))+3)
    #print(len(A)-len(set(A))+4)
    #print(len(A)-len(set(A))+5)
    #print(len(A)-len(set(A))+6)
    #print(len(A)-len(set(A))+7)
    #print(len(A)-len(set(A))+8)
    #print(len(A)-len(set(A))+9)
    #print(len(A)-len(set(A))+10)
    #print(len(A)-len(set(A))+11)
    #print(len(A)-len(set(A))+12)
    #print(len(A)-len(set(A))+13)
    #print(len(A)-len(set(A))+14)
    #print(len(A)-len(set(A))+15)
    #print(len(A)-len(set(A))+16)
    #print(len(A)-len(set(A))+17)
    #print(len(A)-len(set(A))+18)
    #print(len(A)-len(set(A))+19)
    #print(len(A)-len(set(A))+20)
    #print(len(A)-len(set(A))+21)
    #print(len(A)-len(set(A))+22)
    #print(len(A)-len(set(A))+23)
    #print(len(A)-len(set(A))+24)
    #print(len(A)-len(set(A))+25)
    #print(len(A)-len(set(A))+26)
    #print(len(A)-len(set(A))+27)
    #print(len(A)-len(set(A))+28)
    #print(len(A)-len(set(A))+29)
    #print(len(A)-len(set(A))+30)
    #print(len(A)-len(set(A))+31)
    #print(len(A)-len(set(A))+32)
    #print(len(A)-len(set(A))+33)
    #print
