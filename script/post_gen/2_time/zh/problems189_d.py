Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for l in range(n):
        x=a[l]
        for r in range(l,n):
            x=min(x,a[r])
            ans=max(ans,x*(r-l+1))
    print(ans)

=======
Suggestion 2

def main():
    # N = 6
    # A = [2, 4, 4, 9, 4, 9]
    N = 6
    A = [200, 4, 4, 9, 4, 9]
    # N = int(input())
    # A = list(map(int, input().split()))
    max = 0
    for i in range(N):
        for j in range(i, N):
            min = 100000
            for k in range(i, j+1):
                if A[k] < min:
                    min = A[k]
            if min * (j - i + 1) > max:
                max = min * (j - i + 1)
    print(max)

=======
Suggestion 3

def main():
    # 读取输入
    n = int(input())
    a = list(map(int, input().split()))

    # 计算答案
    ans = 0
    for i in range(n):
        for j in range(i, n):
            x = min(a[i:j+1])
            ans = max(ans, x*(j-i+1))

    # 输出答案
    print(ans)

=======
Suggestion 4

def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            x = min(a[i:j+1])
            ans = max(ans, x*(j-i+1))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split(" ")))
    max = 0
    for l in range(1,N+1):
        for r in range(l,N+1):
            for x in range(1,100000):
                if x > max:
                    flag = True
                    for i in range(l-1,r):
                        if x > A[i]:
                            flag = False
                            break
                    if flag:
                        max = x
    print(max)

=======
Suggestion 7

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    max = 0
    for i in range(n):
        for j in range(i,n):
            min = 100000
            for k in range(i,j+1):
                if arr[k] < min:
                    min = arr[k]
            if max < min*(j-i+1):
                max = min*(j-i+1)
    print(max)

=======
Suggestion 8

def get_max_orange_number(orange_list):
    max_orange_number = 0
    for i in range(0, len(orange_list)):
        for j in range(i, len(orange_list)):
            for k in range(1, orange_list[j] + 1):
                if k > max_orange_number:
                    max_orange_number = k
    return max_orange_number
