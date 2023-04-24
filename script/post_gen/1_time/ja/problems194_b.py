Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a_min = min(a)
    b_min = min(b)
    a_min_index = a.index(a_min)
    b_min_index = b.index(b_min)
    if a_min_index == b_min_index:
        a.remove(a_min)
        b.remove(b_min)
        a_second_min = min(a)
        b_second_min = min(b)
        print(min(a_min + b_second_min, a_second_min + b_min))
    else:
        print(max(a_min, b_min))

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    min_a = min(a)
    min_b = min(b)
    if a.index(min_a) != b.index(min_b):
        print(min(min_a, min_b))
    else:
        a.pop(a.index(min_a))
        b.pop(b.index(min_b))
        print(min(min_a+min(b), min_b+min(a)))

=======
Suggestion 3

def main():
    #入力
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #処理
    A_min = min(A)
    B_min = min(B)
    A_min_index = A.index(A_min)
    B_min_index = B.index(B_min)
    if A_min_index == B_min_index:
        A.remove(A_min)
        B.remove(B_min)
        A_min = min(A)
        B_min = min(B)
    #出力
    print(min(A_min + B_min, max(A_min, B_min)))

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[0] > B[0]:
        print(B[0])
    else:
        print(A[0])

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 10**5
    for i in range(N):
        for j in range(N):
            ans = min(ans, max(A[i], B[j]))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_time = 10**5 * N
    for i in range(N):
        for j in range(N):
            if i == j:
                time = A[i] + B[j]
            else:
                time = max(A[i], B[j])
            if time < min_time:
                min_time = time
    print(min_time)

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    min_time = 10 ** 9
    for i in range(N):
        for j in range(N):
            if i == j:
                min_time = min(min_time, A[i] + B[j])
            else:
                min_time = min(min_time, max(A[i], B[j]))
    print(min_time)

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    min_time = 100000
    for i in range(N):
        for j in range(N):
            if i == j:
                time = A[i] + B[j]
            else:
                time = max(A[i],B[j])
            if time < min_time:
                min_time = time
    print(min_time)

=======
Suggestion 9

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int,input().split())
        A.append(a)
        B.append(b)
    min_time = 10**6
    for i in range(N):
        for j in range(N):
            if i == j:
                min_time = min(min_time, A[i]+B[j])
            else:
                min_time = min(min_time, max(A[i],B[j]))
    print(min_time)

=======
Suggestion 10

def main():
    #従業員数
    N = int(input())
    #A_i, B_i
    A_B = [list(map(int, input().split())) for i in range(N)]
    #A_i, B_iの最小値を格納するリスト
    min_A_B = []
    #A_i, B_iの最小値を格納するリストの作成
    for i in range(N):
        min_A_B.append(min(A_B[i]))
    #A_i, B_iの最小値を格納するリストの最小値を出力
    print(min(min_A_B))
