Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 2

def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 3

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    cnt = 0
    for i in range(n):
        if arr[i] != arr[i-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    # 输入
    N = int(input())
    a = list(map(int, input().split()))
    # 处理
    a.sort()
    # 输出
    print(len(set(a)))

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int,input().split()))
    print(len(set(a)))

main()

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 1
    for i in range(1, n):
        if a[i-1] != a[i]:
            count += 1
    print(count)
