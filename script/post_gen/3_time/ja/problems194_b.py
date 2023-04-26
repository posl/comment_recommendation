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
        a_min2 = min(a)
        b_min2 = min(b)
        print(min(a_min + b_min2, a_min2 + b_min))
    else:
        print(a_min + b_min)

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_time = 10**5 * 2
    for i in range(N):
        for j in range(N):
            time = max(A[i], B[j])
            if time < min_time:
                min_time = time
    print(min_time)

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_time = 10**10
    for i in range(N):
        for j in range(N):
            if i == j:
                min_time = min(min_time, A[i]+B[j])
            else:
                min_time = min(min_time, max(A[i], B[j]))
    print(min_time)

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
    min_time = 10**5 * 2
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
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    Amin = min(A)
    Bmin = min(B)
    for i in range(N):
        if A[i] == Amin and B[i] == Bmin:
            print(min(Amin + Bmin, max(Amin, Bmin), max(Amin, Bmin)))
            break
        elif A[i] == Amin or B[i] == Bmin:
            print(max(Amin, Bmin))
            break

=======
Suggestion 6

def main():
    N = int(input())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    min_time = 10**10
    for i in range(N):
        for j in range(N):
            if i == j:
                min_time = min(min_time, A[i] + B[j])
            else:
                min_time = min(min_time, max(A[i], B[j]))
    print(min_time)

=======
Suggestion 7

def main():
    n = int(input())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ans = 10**9
    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i]+b[j])
            else:
                ans = min(ans, max(a[i], b[j]))
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_time = min(A) + min(B)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                time = max(A[i], B[j])
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
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    min_time = 10**6
    for i in range(N):
        for j in range(N):
            if i == j:
                time = A[i]+B[j]
            else:
                time = max(A[i],B[j])
            if min_time > time:
                min_time = time
    print(min_time)

=======
Suggestion 10

def main():
    N = int(input())
    #N個の従業員のA_i,B_iをリストに格納
    A_B = [list(map(int,input().split())) for _ in range(N)]
    #A_i,B_iをそれぞれリストに格納
    A = [A_B[i][0] for i in range(N)]
    B = [A_B[i][1] for i in range(N)]
    #A_i,B_iの最小値をそれぞれ求める
    A_min = min(A)
    B_min = min(B)
    #A_i,B_iの最小値の和
    A_B_min = A_min + B_min
    #A_i,B_iのリストの中でA_B_minより小さい数があるかを確認
    if A_B_min > min(A+B):
        print(A_B_min)
    else:
        print(min(A+B))
