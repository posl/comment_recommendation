Synthesizing 10/10 solutions

=======
Suggestion 1

def f(x):
    if x%2==0:
        return x/2
    elif x%3==0:
        return x/3
    else:
        return -1

n = int(input())
a = list(map(int,input().split()))
ans = 0
while True:
    flag = True
    for i in range(n):
        if f(a[i])!=-1:
            a[i] = f(a[i])
            flag = False
    if flag:
        break
    ans += 1
for i in range(n):
    if a[i]!=a[0]:
        ans = -1
        break
print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        B = []
        for a in A:
            if a % 2 == 0:
                B.append(a // 2)
            elif a % 3 == 0:
                B.append(a // 3)
            else:
                B.append(a)
        if A == B:
            break
        A = B
        ans += 1
    for a in A:
        if a != A[0]:
            print(-1)
            return
    print(ans)
solve()

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    while True:
        if all([i % 2 == 0 for i in a]):
            ans += 1
            a = [i / 2 for i in a]
        else:
            break

    print(ans)

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    while True:
        flag = True
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
                res += 1
                flag = False
                break
        if flag:
            break
    while True:
        flag = True
        for i in range(n):
            if a[i] % 3 == 0:
                a[i] = a[i] / 3
                res += 1
                flag = False
                break
        if flag:
            break
    for i in range(n):
        if a[i] != a[0]:
            print(-1)
            return
    print(res)

=======
Suggestion 5

def divide2(n):
    return n/2

=======
Suggestion 6

def solve(n, a):
    count = 0
    while True:
        if all([i%2==0 for i in a]):
            a = [i/2 for i in a]
            count += 1
        elif all([i%3==0 for i in a]):
            a = [i/3 for i in a]
            count += 1
        elif all([i==a[0] for i in a]):
            return count
        else:
            return -1

n = int(raw_input())
a = map(int, raw_input().split())
print solve(n, a)

=======
Suggestion 7

def check():
    for i in range(1,N):
        if A[i] != A[i-1]:
            return False
    return True

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int,input().split()))
    
    count = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] // 2
            else:
                break
        else:
            count += 1
            continue
        break
    print(count)
main()

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        if sum([a%2 for a in A]) == 0:
            A = [a/2 for a in A]
            count += 1
        else:
            break
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    count = 0
    while True:
        if all([x % 2 == 0 for x in a]):
            a = [x / 2 for x in a]
            count += 1
        elif all([x % 3 == 0 for x in a]):
            a = [x / 3 for x in a]
            count += 1
        else:
            break
    print(count if all([x == a[0] for x in a]) else -1)
