Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[i] != i+1:
            count += 1
    if count > 2:
        print('NO')
    else:
        print('YES')

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if p[i] == i + 1:
            count += 1
    if count == n:
        print("YES")
    elif count == n - 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 'YES'
    for i in range(n):
        if p[i] != i+1:
            ans = 'NO'
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    cnt = 0
    for i in range(n):
        if p[i] != i + 1:
            cnt += 1
    if cnt <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if p[i] != i + 1:
            cnt += 1
    if cnt <= 2:
        print('YES')
    else:
        print('NO')

=======
Suggestion 6

def main():
    N = int(input())
    p = list(map(int, input().split()))
    #print(N, p)
    #print(p.index(1))
    #print(p.index(N))
    if p.index(1) < p.index(N):
        print("YES")
    else:
        print("NO")

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = sorted(p)
    if p == q:
        print("YES")
    else:
        for i in range(n):
            for j in range(i + 1, n):
                if p[i] > p[j]:
                    p[i], p[j] = p[j], p[i]
                    if p == q:
                        print("YES")
                        return
                    else:
                        p[i], p[j] = p[j], p[i]
        print("NO")

=======
Suggestion 8

def main():
    N = int(input())
    p = list(map(int,input().split()))
    #print(N)
    #print(p)
    count = 0
    for i in range(N):
        if p[i] != i + 1:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int,input().split()))
    count = 0
    for i in range(n-1):
        if p[i] != i+1:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 10

def is_sortable(p):
    # p = [5,2,3,4,1]
    # p = [2,4,3,5,1]
    # p = [1,2,3,4,5,6,7]
    # p = [5,4,3,2,1]
    # p = [1,2,3,4,5,7,6]
    # p = [5,2,3,4,1]
    # p = [1,2,3,4,6,5,7]
    # p = [1,2,3,4,6,5,7]
    # p = [1,2,3,4,5,7,6]
    # p = [1,2,3,4,5,6,7]
    # p = [1,2,3,4,5,6,7]
    # p = [1,2,3,4,5,6,7]
    # p = [1,2,3,4,5,6,7]
    # p = [1,2,3,4,5,6,7]
    # p = [1,2,3,4,5,6,7]
    # p = [1,2,3,4,5,6,7]
    # p = [5,2,3,4,1]
    # p = [1,2,3,4,5,6,7]
    # p = [1,2,3,4,5,6,7]
    # p = [1,2,3,4,5,6,7]
    # p = [1,2,3,4,5,6,7]
    # p = [5,2,3,4,1]
    # p = [1,2,3,4,5,6,7]
    # p = [5,2,3,4,1]
    # p = [1,2,3,4,5,6,7]
    # p = [5,2,3,4,1]
    # p = [1,2,3,4,5,6,7]
    # p = [5,2,3,4,1
