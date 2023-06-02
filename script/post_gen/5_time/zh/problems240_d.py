Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, in

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    ans = []
    for i in range(n):
        if a[i] in s:
            ans.append(len(s))
        else:
            ans.append(len(s) + 1)
            s.add(a[i])
    for i in ans:
        print(i)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if i == 0:
            ans.append(1)
        else:
            ans.append(ans[i - 1] + 1)
        for j in range(i - 1, -1, -1):
            if a[i] == a[j]:
                ans[i] = ans[j]
                break
            elif a[i] < a[j]:
                ans[i] = ans[j] + 1
                break
    print(*ans, sep='\n')

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    cnt = {}
    for i in range(n):
        if a[i] in cnt:
            cnt[a[i]] += 1
        else:
            cnt[a[i]] = 1
        ans[i] = len(cnt)
    for i in range(n):
        print(ans[i])

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * n
    for i in range(n):
        b[a[i]-1] += 1
    for i in range(n):
        print(n - b[a[i]-1] + 1)

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(N):
        b.append(0)
    for i in range(N):
        b[a[i] - 1] += 1
    for i in range(N):
        print(N - b[a[i] - 1] + 1)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = 1
    for i in range(1, N):
        ans[i] = ans[i-1] + 1
        if A[i] == A[i-1]:
            ans[i] -= 1
            if i-2 >= 0:
                ans[i] += ans[i-2]
            else:
                ans[i] += 1
    print(*ans, sep='\n')

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(0)
    for i in a:
        b[i-1] += 1
    for i in b:
        print(i)

=======
Suggestion 9

def main():
    N = int(input())
    a = list(map(int, input().split()))

    #a = [3, 2, 3, 2, 2]
    #a = [2, 3, 2, 3, 3, 3, 2, 3, 3, 2]
    #N = len(a)

    a.reverse()
    a.append(0)
    a.reverse()
    #print(a)
    #print(N)

    ans = [0] * N
    ans[0] = 1
    #print(ans)

    for i in range(1, N):
        if a[i] > a[i-1]:
            ans[i] = ans[i-1] + 1
        elif a[i] == a[i-1]:
            ans[i] = ans[i-1]
        else:
            ans[i] = ans[i-1] - 1

    #print(ans)

    ans.reverse()
    print(*ans, sep='\n')

=======
Suggestion 10

def main():
    N = int(input())
    a = list(map(int, input().split()))

    b = []
    c = []
    for i in range(N):
        b.append(a[i])
        if len(b) >= 2 and b[-2] == b[-1]:
            b.pop()
            b.pop()
        c.append(len(b))
    print("\n".join(map(str, c)))
