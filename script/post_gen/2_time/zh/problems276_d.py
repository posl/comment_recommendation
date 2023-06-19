Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        if all([a[i] % 2 == 0 for i in range(N)]):
            a = [a[i] // 2 for i in range(N)]
            ans += 1
        else:
            break
    print(ans)

    return

=======
Suggestion 2

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    while True:
        if all(x % 2 == 0 for x in A):
            A = [x // 2 for x in A]
            ans += 1
        else:
            break
    print(ans)

solve()

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            elif a[i] % 3 == 0:
                a[i] = a[i] / 3
            else:
                break
        else:
            count += 1
            continue
        break
    if count == 0:
        print(-1)
    else:
        print(count)
main()
#解答1

=======
Suggestion 4

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        if sum([i % 2 for i in a]) != 0:
            break
        a = [i // 2 for i in a]
        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    while True:
        flag = True
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[i] = A[i] / 2
                flag = False
                break

        if flag:
            break

        cnt += 1

    print(cnt)

=======
Suggestion 6

def func(a):
    if a % 2 == 0:
        return a/2
    elif a % 3 == 0:
        return a/3
    else:
        return -1

=======
Suggestion 7

def solve(N, A):
    count = 0
    while True:
        if all(a % 2 == 0 for a in A):
            count += 1
            A = [a / 2 for a in A]
        elif all(a % 3 == 0 for a in A):
            count += 1
            A = [a / 3 for a in A]
        elif all(a == A[0] for a in A):
            break
        else:
            return -1
    return count

N = int(raw_input())
A = map(int, raw_input().split())
print solve(N, A)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        flag = True
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] // 2
            else:
                flag = False
                break
        if flag:
            ans += 1
        else:
            break
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    count = 0
    while True:
        if all([a%2==0 for a in A]):
            A = [a/2 for a in A]
            count += 1
        elif all([a%3==0 for a in A]):
            A = [a/3 for a in A]
            count += 1
        else:
            break
    if all([a==A[0] for a in A]):
        print(count)
    else:
        print(-1)

=======
Suggestion 10

def main():
    n=int(input())
    A=list(map(int,input().split()))
    count=0
    while True:
        flag=0
        for i in range(n):
            if A[i]%2==0:
                A[i]=A[i]/2
                flag=1
            if A[i]%3==2:
                A[i]=A[i]/3
                flag=1
        if flag==1:
            count+=1
        else:
            break
    for i in range(1,n):
        if A[i]!=A[0]:
            count=-1
            break
    print(count)
    
main()
