Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if p[i] != i + 1:
            cnt += 1
    if cnt <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 2

def main():
    N = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if p[i] != i+1:
            cnt += 1
    if cnt <= 2:
        print('YES')
    else:
        print('NO')

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n-1):
        if p[i] > p[i+1]:
            count += 1
            if count >= 2:
                print("NO")
                return
    print("YES")
    return

=======
Suggestion 4

def main():
    N = int(input())
    p = [int(i) for i in input().split()]
    c = 0
    for i in range(N):
        if p[i] != i+1:
            c += 1
    if c <= 2:
        print('YES')
    else:
        print('NO')

=======
Suggestion 5

def main():
    N = int(input())
    p = list(map(int, input().split()))
    if p == sorted(p):
        print("YES")
    elif p[0] == 1 or p[-1] == N:
        print("NO")
    elif p[0] == N and p[-1] == 1:
        print("YES")
    else:
        print("NO")

=======
Suggestion 6

def  main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if p[i] != i + 1:
            count += 1
    if count <= 2:
        print('YES')
    else:
        print('NO')

=======
Suggestion 7

def main():
    N = int(input())
    p = list(map(int, input().split()))
    if p == sorted(p):
        print('YES')
    else:
        if p[0] == 1 or p[-1] == N:
            print('YES')
        else:
            if p[0] == N and p[-1] == 1:
                print('YES')
            else:
                print('NO')

=======
Suggestion 8

def main():
    N = int(input())
    p = list(map(int, input().split()))
    if p == sorted(p):
        print('YES')
    else:
        ans = 'NO'
        for i in range(N):
            for j in range(i + 1, N):
                p[i], p[j] = p[j], p[i]
                if p == sorted(p):
                    ans = 'YES'
                p[i], p[j] = p[j], p[i]
        print(ans)
