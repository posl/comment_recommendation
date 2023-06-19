Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

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

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p_sorted = sorted(p)
    count = 0
    for i in range(len(p)):
        if p[i] != p_sorted[i]:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 4

def main():
    N = int(input())
    p = list(map(int, input().split()))
    #print(N, p)
    count = 0
    for i in range(N):
        if p[i] != i+1:
            count += 1
    if count == 2 or count == 0:
        print("YES")
    else:
        print("NO")

=======
Suggestion 5

def check_sort(p):
    for i in range(len(p)-1):
        if p[i] > p[i+1]:
            return False
    return True

=======
Suggestion 6

def main():
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
    cnt = 0
    for i in range(N):
        if p[i] != i + 1:
            cnt += 1
    if cnt <= 2:
        print('YES')
    else:
        print('NO')

=======
Suggestion 8

def checkSort(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
