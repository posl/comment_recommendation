Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().s

=======
Suggestion 2

def get_input():
    input_str = input()
    input_list = input_str.split()
    n = int(input_list[0])
    k = int(input_list[1])
    input_str = input()
    input_list = input_str.split()
    a_list = []
    for i in range(n):
        a_list.append(int(input_list[i]))
    return n, k, a_list

=======
Suggestion 3

def problems155_d():
    pass

=======
Suggestion 4

def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    l = -10**18-1
    r = 10**18+1
    while l+1<r:
        mid = (l+r)//2
        cnt = 0
        for i in range(n):
            if a[i]<0:
                cnt += n-i-1
                l = mid
            else:
                #二分查找
                l = -1
                r = n
                while l+1<r:
                    m = (l+r)//2
                    if a[i]*a[m]<mid:
                        l = m
                    else:
                        r = m
                cnt += n-r
        if cnt<k:
            l = mid
        else:
            r = mid
    print(l)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    #print(a)
    #print(k)
    #print(n)
    #print(a[k])
    #print(a[k-1])
    #print(a[k-2])
    #print(a[k-3])
    #print(a[k-4])
    #print(a[k-5])
    #print(a[k-6])
    #print(a[k-7])
    #print(a[k-8])
    #print(a[k-9])
    #print(a[k-10])
    #print(a[k-11])
    #print(a[k-12])
    #print(a[k-13])
    #print(a[k-14])
    #print(a[k-15])
    #print(a[k-16])
    #print(a[k-17])
    #print(a[k-18])
    #print(a[k-19])
    #print(a[k-20])
    #print(a[k-21])
    #print(a[k-22])
    #print(a[k-23])
    #print(a[k-24])
    #print(a[k-25])
    #print(a[k-26])
    #print(a[k-27])
    #print(a[k-28])
    #print(a[k-29])
    #print(a[k-30])
    #print(a[k-31])
    #print(a[k-32])
    #print(a[k-33])
    #print(a[k-34])
    #print(a[k-35])
    #print(a[k-36])
    #print(a[k-37])
    #print(a[k-38])
    #print(a[k-39])
    #print(a[k-40])
    #print(a[k-41])
    #print(a[k-42])
    #print(a[k-43])
    #print(a[k-44])
    #print(a[k-45])
    #print(a[k-46])
    #print(a[k-47])
    #print(a[k-48])
    #print(a[k-49])
    #print(a[k-50])
    #print(a[k-51])
    #print(a[k-52])
    #print(a[k-53])
    #print(a[k-54])
    #print(a[k-55])
    #print(a[k-56])
    #print(a[k

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    l = list(map(int,input().split()))

    l.sort()
    print(l[k-1])

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    left = -10**18
    right = 10**18
    while right - left > 1:
        mid = (left + right) // 2
        cnt = 0
        for i in range(n):
            if a[i] >= 0:
                l = -1
                r = n
                while r - l > 1:
                    m = (l + r) // 2
                    if a[i] * a[m] <= mid:
                        r = m
                    else:
                        l = m
                cnt += n - r
            else:
                l = -1
                r = n
                while r - l > 1:
                    m = (l + r) // 2
                    if a[i] * a[m] <= mid:
                        l = m
                    else:
                        r = m
                cnt += r
            if a[i] * a[i] <= mid:
                cnt -= 1
        cnt //= 2
        if cnt < k:
            left = mid
        else:
            right = mid
    print(right)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    left = -10**18
    right = 10**18
    while right - left > 1:
        mid = (left + right) // 2
        cnt = 0
        for i in range(n):
            if a[i] < 0:
                l = -1
                r = n
                while r - l > 1:
                    m = (l + r) // 2
                    if a[i] * a[m] < mid:
                        r = m
                    else:
                        l = m
                cnt += n - r
            elif a[i] == 0:
                if mid > 0:
                    cnt += n
            else:
                l = -1
                r = n
                while r - l > 1:
                    m = (l + r) // 2
                    if a[i] * a[m] < mid:
                        l = m
                    else:
                        r = m
                cnt += r
                cnt += n - r
        cnt //= 2
        if cnt < k:
            left = mid
        else:
            right = mid
    print(left)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    l = -10**18
    r = 10**18
    while r - l > 1:
        mid = (r + l) // 2
        count = 0
        for i in range(N):
            if A[i] < 0:
                l2 = -1
                r2 = N
                while r2 - l2 > 1:
                    mid2 = (r2 + l2) // 2
                    if A[i] * A[mid2] < mid:
                        r2 = mid2
                    else:
                        l2 = mid2
                count += N - r2
            else:
                l2 = -1
                r2 = N
                while r2 - l2 > 1:
                    mid2 = (r2 + l2) // 2
                    if A[i] * A[mid2] < mid:
                        l2 = mid2
                    else:
                        r2 = mid2
                count += r2
            if A[i] * A[i] < mid:
                count -= 1
        if count < K:
            l = mid
        else:
            r = mid
    print(l)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(K)
    #print(N)
    #print(A[K-1])
    #print(A[N-1])
    #print(A[0])
    #print(A[N-1]*A[N-2])
    #print(A[0]*A[1])
    #print(A[N-1]*A[0])
    #print(A[N-1]*A[1])
    #print(A[N-2]*A[0])
    #print(A[N-2]*A[1])
    if K <= ((N*(N-1))/2):
        if A[N-1] >= 0:
            if K == 1:
                print(A[N-1]*A[N-2])
            else:
                print(A[K-1])
        elif A[N-1] < 0:
            if K == ((N*(N-1))/2):
                print(A[0]*A[1])
            else:
                print(A[N-1]*A[0])
    elif K > ((N*(N-1))/2):
        if A[N-1] >= 0:
            print(A[N-1]*A[0])
        elif A[N-1] < 0:
            print(A[N-1]*A[1])
