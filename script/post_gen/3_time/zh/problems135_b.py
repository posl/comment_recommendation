Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    p = list(map(int, input().split()))
    if p == sorted(p):
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
        print("YES")
    else:
        print("NO")

=======
Suggestion 3

def judge(p):
    for i in range(len(p)-1):
        if p[i]>p[i+1]:
            return False
    return True

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n-1):
        if p[i] > p[i+1]:
            count += 1
    if count <= 1:
        print('YES')
    else:
        print('NO')

=======
Suggestion 5

def solve():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N - 1):
        if p[i] == i + 1:
            count += 1
    if count == N - 1:
        print("YES")
    else:
        print("NO")

=======
Suggestion 6

def main():
    N = int(input())
    p = list(map(int, input().split()))

    # 1. 降序排序
    # 2. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 3. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 4. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 5. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 6. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 7. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 8. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 9. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    # 10. 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO

    # 降序排序
    p.sort(reverse=True)

    # 降序排序后的序列 p 与原序列 p 比较，如果相同则输出 YES，否则输出 NO
    if p == list(range(1, N + 1)):
        print('YES')
    else:
        print('NO')

=======
Suggestion 7

def main():
    N = int(input())
    p = list(map(int, input().split()))
    is_sorted = True
    for i in range(N-1):
        if p[i] > p[i+1]:
            is_sorted = False
            break
    if is_sorted:
        print("YES")
    else:
        print("NO")

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p_sort = sorted(p)
    cnt = 0
    for i in range(n):
        if p[i] != p_sort[i]:
            cnt += 1
    if cnt == 0 or cnt == 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 9

def main():
    N = int(input())
    p = [int(i) for i in input().split()]

    if p == sorted(p):
        print("YES")
        return

    for i in range(N):
        for j in range(i+1, N):
            p[i], p[j] = p[j], p[i]
            if p == sorted(p):
                print("YES")
                return
            p[i], p[j] = p[j], p[i]

    print("NO")

=======
Suggestion 10

def main():
    N = int(input())
    p = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if p[i] == i+1:
            count += 1
    if count == N:
        print("YES")
    elif count == N-2:
        print("YES")
    else:
        print("NO")
main()
