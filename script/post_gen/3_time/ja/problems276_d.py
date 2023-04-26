Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt2 = 0
    cnt3 = 0
    for a in A:
        while a % 2 == 0:
            a //= 2
            cnt2 += 1
        while a % 3 == 0:
            a //= 3
            cnt3 += 1
    if all(a == A[0] for a in A):
        print(cnt2 + cnt3)
    else:
        print(-1)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            elif A[i] % 3 == 0:
                A[i] = A[i] // 3
            else:
                count = -1
                break
        if count == -1:
            break
        count += 1
        if all([A[0] == A[i] for i in range(1, N)]):
            break
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 3 == 0:
                A[i] = A[i] // 3
                count += 1
            else:
                break
        else:
            continue
        break
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
                count += 1
            else:
                break
        else:
            continue
        break
    for i in range(N):
        if A[i] != A[0]:
            count = -1
            break
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    two = 0
    three = 0
    for a in A:
        while a % 2 == 0:
            a //= 2
            two += 1
        while a % 3 == 0:
            a //= 3
            three += 1
        if a != 1:
            print(-1)
            return
    print(two + three)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            else:
                break
        else:
            count += 1
            continue
        break
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i]%2 == 0:
                A[i] = A[i]/2
            elif A[i]%3 == 0:
                A[i] = A[i]/3
            else:
                count = -1
                break
        if count == -1:
            break
        if len(set(A)) == 1:
            break
        count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        if all(a % 2 == 0 for a in A):
            A = [a // 2 for a in A]
            ans += 1
        else:
            break
    while True:
        if all(a % 3 == 0 for a in A):
            A = [a // 3 for a in A]
            ans += 1
        else:
            break
    if all(a == A[0] for a in A):
        print(ans)
    else:
        print(-1)

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    count = 0
    while True:
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[i] = A[i] / 2
            elif A[i] % 3 == 0:
                A[i] = A[i] / 3
            else:
                print(-1)
                return
        if len(set(A)) == 1:
            print(count)
            return
        count += 1

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != A[N-1]:
        print(-1)
    else:
        ans = 0
        while A[0] % 2 == 0:
            A[0] = A[0] // 2
            ans += 1
        while A[0] % 3 == 0:
            A[0] = A[0] // 3
            ans += 1
        if A[0] == 1:
            print(ans)
        else:
            print(-1)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int,input().split()))
    cnt = 0
    while True:
        if all(a%2==0 for a in A):
            A = [a//2 for a in A]
            cnt += 1
        else:
            break
    if all(a==A[0] for a in A):
        print(cnt)
    else:
        print(-1)
