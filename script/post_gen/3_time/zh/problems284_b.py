Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    T = int(input())
    A = []
    for i in range(T):
        N = int(input())
        A.append(N)
        A.append(input().split())
    # 处理
    for i in range(T):
        count = 0
        for j in range(int(A[2*i])):
            if int(A[2*i+1][j]) % 2 == 1:
                count += 1
        # 输出结果
        print(count)

=======
Suggestion 2

def problems284_b():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        cnt = 0
        for j in range(N):
            if A[j] % 2 != 0:
                cnt += 1
        print(cnt)

=======
Suggestion 3

def problems284_b():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        count = 0
        for i in range(n):
            if a[i] % 2 == 1:
                count += 1
        print(count)

=======
Suggestion 4

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        cnt = 0
        for j in range(n):
            if a[j] % 2 == 1:
                cnt += 1
        print(cnt)

=======
Suggestion 5

def count_odd():
    num = int(input())
    num_list = input().split()
    count = 0
    for i in range(num):
        if int(num_list[i]) % 2 != 0:
            count += 1
    print(count)

=======
Suggestion 6

def problems284_b():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        result = 0
        for j in range(N):
            if A[j] % 2 == 1:
                result += 1
        print(result)

=======
Suggestion 7

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = input().split()
        count = 0
        for i in range(N):
            if int(A[i]) % 2 == 1:
                count += 1
        print(count)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if a[i] % 2 == 1:
            cnt += 1
    print(cnt)

=======
Suggestion 9

def count_odd_number(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 1:
            count += 1
    return count

=======
Suggestion 10

def problems284_b():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        count = 0
        for j in range(N):
            if A[j] % 2 == 1:
                count += 1
        print(count)
