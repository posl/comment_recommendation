Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 入力
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 高橋氏の票数を計算
    T = 0
    for i in range(N):
        T += B[i]

    # 青木氏の票数を計算
    A.sort()
    B.sort()
    A.reverse()
    B.reverse()
    S = 0
    for i in range(N):
        S += A[i]
        if S > T:
            print(i + 1)
            return

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    A.append(0)
    B.append(0)
    A_sum = [0]
    B_sum = [0]
    for a in A:
        A_sum.append(A_sum[-1] + a)
    for b in B:
        B_sum.append(B_sum[-1] + b)
    ans = 10**9
    for i in range(N + 1):
        a = A_sum[i]
        b = B_sum[N] - B_sum[i]
        if a < b:
            ans = min(ans, i)
    print(ans)

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
    #print(A)
    #print(B)
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    ans = 0
    for i in range(N):
        ans += max(A[i], B[i])
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    diff = [a-b for a, b in zip(A, B)]
    diff.sort(reverse=True)
    
    count = 0
    for i in range(N):
        count += diff[i]
        if count > 0:
            print(i+1)
            exit()

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    #print(A)
    #print(B)
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    if A[-1] > B[-1]:
        print(0)
    else:
        print(B[-1] - A[-1] + 1)

=======
Suggestion 6

def main():
    N = int(input())
    AB = []
    for _ in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    A = 0
    B = 0
    for i in range(N):
        if i % 2 == 0:
            A += AB[i][0]
        else:
            B += AB[i][1]
    print(A - B)

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for n in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(A[0])
    #print(B[0])
    #print(A[0] + B[0])
    #print(A[0] - B[0])
    #print(abs(A[0] - B[0]))
    #print(A[0] - B[0] < 0)
    #print(A[0] - B[0] > 0)
    #print(A[0] - B[0] == 0)
    #print(A[0] - B[0] < 0)
    #print(A[0] - B[0] > 0)
    #print(A[0] - B[0] == 0)
    #print(A[0] - B[0] < 0)
    #print(A[0] - B[0] > 0)
    #print(A[0] - B[0] == 0)
    #print(A[0] - B[0] < 0)
    #print(A[0] - B[0] > 0)
    #print(A[0] - B[0] == 0)
    #print(A[0] - B[0] < 0)
    #print(A[0] - B[0] > 0)
    #print(A[0] - B[0] == 0)
    #print(A[0] - B[0] < 0)
    #print(A[0] - B[0] > 0)
    #print(A[0] - B[0] == 0)
    #print(A[0] - B[0] < 0)
    #print(A[0] - B[0] > 0)
    #print(A[0] - B[0] == 0)
    #print(A[0] - B[0] < 0)
    #print(A[0] - B[0] > 0)
    #print(A[0] - B[0] == 0)
    #print(A[0] - B[

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
    C = [A[i] + B[i] for i in range(N)]
    C.sort(reverse = True)
    ans = 0
    for i in range(N):
        if i%2 == 0:
            ans += C[i]
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    #print(AB)
    A, B = 0, 0
    for i in range(N):
        if i % 2 == 0:
            A += AB[i][0]
        else:
            B += AB[i][1]
    print(A - B)

=======
Suggestion 10

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] - x[1], reverse=True)
    ans = 0
    for a, b in AB:
        if a >= b:
            ans += 1
        else:
            break
    print(ans)
