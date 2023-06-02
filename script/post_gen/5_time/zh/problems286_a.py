Synthesizing 10/10 solutions

=======
Suggestion 1

def swap(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left = left + 1
        right = right - 1

=======
Suggestion 2

def main():
    # 读取数据
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    # 交换
    b = a[0:p-1]+a[r-1:s]+a[q-1:r-1]+a[p-1:q-1]+a[s:]
    # 打印
    for i in range(n):
        if i == n-1:
            print(b[i])
        else:
            print(b[i], end=" ")

=======
Suggestion 3

def exchange(a, b, c, d, e):
    for i in range(b-1, c):
        a[i], a[d+i-c+1] = a[d+i-c+1], a[i]
    return a

=======
Suggestion 4

def swap(arr, p, q, r, s):
    arr1 = arr[p : q + 1]
    arr2 = arr[r : s + 1]
    arr[p : q + 1] = arr2
    arr[r : s + 1] = arr1
    return arr

=======
Suggestion 5

def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

=======
Suggestion 6

def swap_list(list1, p, q, r, s):
    list2 = list1[p-1:q] + list1[r-1:s]
    list2.reverse()
    list1[p-1:q] = list2[0:q-p+1]
    list1[r-1:s] = list2[q-p+1:]
    return list1

=======
Suggestion 7

def exchange(a,p,q,r,s):
    b = a.copy()
    for i in range(q-p+1):
        b[p+i-1] = a[s+i-1]
        b[s+i-1] = a[p+i-1]
    return b

=======
Suggestion 8

def swap(A, P, Q, R, S):
    B = []
    B.extend(A)
    for i in range(P-1, Q):
        B[i] = A[R-1+i-Q]
    for i in range(R-1, S):
        B[i] = A[P-1+i-R+Q]
    return B

=======
Suggestion 9

def main():
    #读取输入
    n,p,q,r,s = map(int,input().split())
    a = list(map(int,input().split()))

    #解决问题
    b = a.copy()
    for i in range(p-1,q):
        b[i] = a[r-1+i-q]
    for i in range(r-1,s):
        b[i] = a[p-1+i-r]

    #输出结果
    print(*b)

=======
Suggestion 10

def swap(a, b):
    return b, a

N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))

for i in range(P-1, Q):
    A[i], A[i+R-Q] = swap(A[i], A[i+R-Q])

print(' '.join(map(str, A)))
