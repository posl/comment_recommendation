Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if p[i] != i+1:
            cnt += 1
    if cnt == 2 or cnt == 0:
        print("YES")
    else:
        print("NO")

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if p[i] != i+1:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 3

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
Suggestion 4

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[i] != i+1:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p_sorted = sorted(p)
    cnt = 0
    for i in range(n):
        if p[i] != p_sorted[i]:
            cnt += 1
    if cnt <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 6

def main():
    N = int(input())
    p = list(map(int,input().split()))
    p_sort = sorted(p)
    count = 0
    for i in range(N):
        if p[i] != p_sort[i]:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.sort()
    cnt = 0
    for i in range(n):
        if p[i] != i+1:
            cnt += 1
    if cnt <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 8

def check_sort(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

N = int(input())
p_list = list(map(int, input().split()))
for i in range(N):
    for j in range(i+1, N):
        p_list[i], p_list[j] = p_list[j], p_list[i]
        if check_sort(p_list):
            print("YES")
            exit()
        p_list[i], p_list[j] = p_list[j], p_list[i]
print("NO")

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    for i in range(n):
        if p[i] == i+1:
            continue
        if i+1 in p:
            j = p.index(i+1)
            p[i], p[j] = p[j], p[i]
        else:
            print('NO')
            return
    print('YES')
