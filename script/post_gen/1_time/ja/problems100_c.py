Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if a[i] % 2 == 0:
                a[i] = a[i] // 2
            else:
                print(count)
                return
        count += 1

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        while a % 2 == 0:
            a = a // 2
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            else:
                print(ans)
                return
        ans += 1

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 1:
                print(cnt)
                return
            else:
                A[i] = A[i] // 2
        cnt += 1

=======
Suggestion 5

def main():
    N = int(input())
    a = list(map(int,input().split()))
    count = 0
    while True:
        for i in range(N):
            if a[i] % 2 == 1:
                print(count)
                return
            a[i] //= 2
        count += 1

main()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in A:
        while i % 2 == 0:
            ans += 1
            i //= 2
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        while True:
            if a % 2 == 0:
                a //= 2
                ans += 1
            else:
                break
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    while all([i % 2 == 0 for i in a]):
        cnt += 1
        a = [i // 2 for i in a]
    print(cnt)

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    a = list(map(int,input().split()))
    
    cnt = 0
    while True:
        for i in range(N):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            else:
                print(cnt)
                return
        cnt += 1

=======
Suggestion 10

def main():
    #N
    N = int(input())
    #a_1 a_2 a_3 ... a_N
    a = [int(s) for s in input().split()]
    #print(a)
    cnt = 0
    while True:
        for i in range(N):
            if a[i] % 2 == 0:
                a[i] = a[i] // 2
            else:
                break
        else:
            cnt += 1
            continue
        break
    print(cnt)
