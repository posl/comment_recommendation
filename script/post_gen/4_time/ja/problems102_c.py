Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = a[n//2]
    ans = 0
    for i in range(n):
        ans += abs(a[i] - b)
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = a[n//2]
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (b + i + 1))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - (i + 1)
    B.sort()
    b = B[N // 2]
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (b + i + 1))
    print(ans)

=======
Suggestion 4

def get_ans(n, a):
    a.sort()
    b = a[n//2]
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (b+i))
    return ans

n = int(input())
a = list(map(int, input().split()))
print(get_ans(n, a))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # すぬけ君の悲しさの値の最小値は、
    # 中央値になる
    A.sort()
    B = []
    for i in range(N):
        B.append(A[i] - (i+1))
    B.sort()
    b = B[N//2]
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (b+i+1))
    print(ans)

=======
Suggestion 6

def get_input_data():
    n = int(input())
    a_list = list(map(int, input().split()))
    return n, a_list

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    
    if N%2 == 0:
        #print(N//2)
        b = A[N//2] - 1
    else:
        #print(N//2)
        b = A[N//2]
    #print(b)
    ans = 0
    for i in range(N):
        ans += abs(A[i] - (b+i+1))
    print(ans)
