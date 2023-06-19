Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    xk = []
    for _ in range(q):
        xk.append(list(map(int, input().split())))
    return n, q, a, xk

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(Q):
        x, k = map(int, input().split())
        print(find_kth(A, x, k))

=======
Suggestion 3

def get_index(num, k, list):
    count = 0
    for i in range(len(list)):
        if list[i] == num:
            count += 1
            if count == k:
                return i + 1
    return -1

=======
Suggestion 4

def find_kth_number_in_array(arr, x, k):
    if arr.count(x) < k:
        return -1
    else:
        count = 0
        for i in range(0, len(arr)):
            if arr[i] == x:
                count += 1
                if count == k:
                    return i+1
        return -1

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        tmp = 0
        for j in range(N):
            if A[j] == x:
                k -= 1
            if k == 0:
                tmp = j
                break
        if tmp:
            print(tmp+1)
        else:
            print(-1)

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        count = 0
        for j in range(n):
            if a[j] == x:
                count += 1
            if count == k:
                print(j+1)
                break
        if count < k:
            print(-1)

=======
Suggestion 7

def binary_search(a, x, k):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            if mid == 0 or a[mid - 1] != x:
                return mid + 1
            else:
                high = mid - 1
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

=======
Suggestion 8

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(q):
        x,k = map(int,input().split())
        cnt = 0
        for j in range(n):
            if a[j] == x:
                cnt += 1
            if cnt == k:
                print(j+1)
                break
        else:
            print(-1)

=======
Suggestion 9

def problem235_c():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        count = 0
        for j in range(n):
            if a[j] == x:
                count += 1
                if count == k:
                    print(j+1)
                    break
        else:
            print(-1)

=======
Suggestion 10

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(Q):
        x, k = map(int, input().split())
        cnt = 0
        for i in range(N):
            if A[i] == x:
                cnt += 1
                if cnt == k:
                    print(i + 1)
                    break
        else:
            print(-1)

solve()
