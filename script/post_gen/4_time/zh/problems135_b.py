Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    p = list(map(int, input().split()))
    #print(N)
    #print(p)
    p_sort = sorted(p)
    #print(p_sort)
    cnt = 0
    for i in range(N):
        if p[i] != p_sort[i]:
            cnt += 1
    if cnt == 2 or cnt == 0:
        print("YES")
    else:
        print("NO")

=======
Suggestion 2

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[i] != i + 1:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")
main()

=======
Suggestion 3

def main():
    # N = int(input())
    # p = list(map(int,input().split()))
    N = 5
    p = [2, 4, 3, 5, 1]
    # N = 7
    # p = [1, 2, 3, 4, 5, 6, 7]
    cnt = 0
    for i in range(N):
        if p[i] != i+1:
            cnt += 1
    if cnt <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 4

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[i] != i+1:
            count += 1
    if count == 2 or count == 0:
        print('YES')
    else:
        print('NO')

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n):
        if p[i-1] > p[i]:
            cnt += 1
    if cnt <= 2:
        print('YES')
    else:
        print('NO')

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if p[i] != i+1:
            count += 1
    if count == 2 or count == 0:
        print('YES')
    else:
        print('NO')

=======
Suggestion 7

def main():
    N = int(input())
    p = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        if p[i] != i+1:
            count += 1
    if count <= 2:
        print('YES')
    else:
        print('NO')

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if p[i] > p[j]:
                count += 1
    if count <= 1:
        print("YES")
    else:
        print("NO")

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if i + 1 != p[i]:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 10

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    count = 0
    for i in range(n):
        if p[i] != i+1:
            count += 1
    if count <= 2:
        print('YES')
    else:
        print('NO')
