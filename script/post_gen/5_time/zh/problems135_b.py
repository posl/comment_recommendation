Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    p = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        if i+1 != p[i]:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 2

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    count = 0
    for i in range(n):
        if p[i] != i + 1:
            count += 1
    if count > 2:
        print("NO")
    else:
        print("YES")

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        if p[i] != i+1:
            cnt += 1
    if cnt <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int,input().split()))
    count = 0
    for i in range(n):
        if p[i] != i+1:
            count += 1
    if count <= 2:
        print('YES')
    else:
        print('NO')

=======
Suggestion 5

def check_sort(p):
    for i in range(len(p)):
        if p[i] != i + 1:
            return False
    return True

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if i+1 != p[i]:
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
    sorted_p = sorted(p)
    if p == sorted_p:
        print('YES')
    else:
        for i in range(n):
            for j in range(i+1, n):
                p[i], p[j] = p[j], p[i]
                if p == sorted_p:
                    print('YES')
                    return
                else:
                    p[i], p[j] = p[j], p[i]
        print('NO')

=======
Suggestion 8

def main():
    num = int(input())
    input_list = list(map(int, input().split()))
    for i in range(num):
        if input_list[i] == i+1:
            continue
        else:
            if input_list[i] == i+2 and input_list[i+1] == i+1:
                continue
            else:
                print('NO')
                return
    print('YES')
    return
