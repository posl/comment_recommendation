Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        cnt = 0
        for j in range(n):
            if a[j] == x:
                cnt += 1
            if cnt == k:
                print(j+1)
                break
        else:
            print(-1)
main()

=======
Suggestion 2

def main():
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

=======
Suggestion 3

def binary_search(arr, x, k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            if mid == k - 1:
                return mid
            elif mid > k - 1:
                right = mid - 1
            else:
                left = mid + 1
    return -1

n, q = map(int,input().split())
a = list(map(int,input().split()))
for _ in range(q):
    x, k = map(int,input().split())
    print(binary_search(a, x, k) + 1)

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    #print(a)
    for i in range(q):
        x, k = map(int, input().split())
        #print(x, k)
        count = 0
        for j in range(n):
            if a[j] == x:
                count += 1
            if count == k:
                print(j + 1)
                break
        else:
            print(-1)

=======
Suggestion 5

def find_value(a, x, k):
    result = -1
    count = 0
    for i in range(len(a)):
        if a[i] == x:
            count += 1
            if count == k:
                result = i + 1
                break
    return result

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        cnt = 0
        for j in range(N):
            if A[j] == x:
                cnt += 1
                if cnt == k:
                    print(j + 1)
                    break
        else:
            print(-1)

=======
Suggestion 7

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
