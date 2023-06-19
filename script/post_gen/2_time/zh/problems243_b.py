Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    # print(A)
    # print(B)
    count1 = 0
    count2 = 0
    for i in range(N):
        if A[i] == B[i]:
            count1 += 1
    for i in range(N):
        for j in range(N):
            if i != j and A[i] == B[j]:
                count2 += 1
    print(count1)
    print(count2)

=======
Suggestion 2

def main():
    # 读入数据
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 处理数据
    # 1. 包含在A和B中的整数的数量，出现在两个序列的相同位置
    # 2. 包含在A和B中的整数的数量，出现在两个序列的不同位置
    count1 = 0
    count2 = 0
    for i in range(N):
        if A[i] == B[i]:
            count1 += 1
    for i in range(N):
        for j in range(N):
            if i != j and A[i] == B[j]:
                count2 += 1
    # 输出结果
    print(count1)
    print(count2)

=======
Suggestion 3

def main():
    N = int(input())
    A = input().split()
    B = input().split()
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        if A[i] == B[i]:
            cnt1 += 1
    for i in range(N):
        for j in range(N):
            if A[i] == B[j] and i != j:
                cnt2 += 1
    print(cnt1)
    print(cnt2)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = 0
    d = 0
    for i in range(n):
        if a[i] == b[i]:
            c += 1
    for i in range(n):
        for j in range(n):
            if i != j and a[i] == b[j]:
                d += 1
    print(c)
    print(d)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count1 = 0
    count2 = 0
    for i in range(n):
        if a[i] == b[i]:
            count1 += 1
    for i in range(n):
        for j in range(n):
            if a[i] == b[j] and i != j:
                count2 += 1
    print(count1)
    print(count2)

=======
Suggestion 6

def get_same_num(a_list, b_list):
    same_num = 0
    for i in range(len(a_list)):
        if a_list[i] in b_list and a_list[i] == b_list[i]:
            same_num += 1
    return same_num

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count1 = 0
    count2 = 0
    for i in range(n):
        if a[i] == b[i]:
            count1 += 1
    for i in range(n):
        for j in range(n):
            if i != j and a[i] == b[j]:
                count2 += 1
    print(count1)
    print(count2)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count1 = 0
    count2 = 0
    for i in range(n):
        if a[i] == b[i]:
            count1 += 1
    for i in range(n):
        for j in range(n):
            if a[i] == b[j] and i != j:
                count2 += 1
    print(count1)
    print(int(count2/2))

=======
Suggestion 9

def main():
    n = int(input())
    a = input().split()
    b = input().split()
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    count_1 = 0
    count_2 = 0
    for i in range(n):
        if a[i] == b[i]:
            count_1 += 1
    for i in range(n):
        for j in range(n):
            if a[i] == b[j] and i != j:
                count_2 += 1
    print(count_1)
    print(count_2)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans1 = 0
    ans2 = 0
    for i in range(n):
        if a[i] == b[i]:
            ans1 += 1
    for i in range(n):
        for j in range(n):
            if i != j:
                if a[i] == b[j]:
                    ans2 += 1
    print(ans1)
    print(ans2)
