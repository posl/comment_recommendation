Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for l in range(N):
        x = A[l]
        for r in range(l, N):
            x = min(x, A[r])
            ans = max(ans, x * (r - l + 1))
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        l = i
        r = i
        x = a[i]
        while l > 0 and a[l-1] >= x:
            l -= 1
        while r < n-1 and a[r+1] >= x:
            r += 1
        ans = max(ans, x*(r-l+1))
    print(ans)

=======
Suggestion 3

def max_orange(orange_list):
    max_num = 0
    for i in range(len(orange_list)):
        for j in range(i,len(orange_list)):
            for k in range(1,orange_list[j]+1):
                if k > max_num and min(orange_list[i:j+1]) >= k:
                    max_num = k
    return max_num

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        x = a[i]
        for j in range(i, n):
            x = min(x, a[j])
            ans = max(ans, x * (j - i + 1))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for l in range(N):
        x = A[l]
        for r in range(l, N):
            x = min(x, A[r])
            ans = max(ans, x * (r - l + 1))

    print(ans)

=======
Suggestion 6

def get_max_orange_count(orange_count_list):
    max_orange_count = 0
    for i in range(len(orange_count_list)):
        for j in range(i, len(orange_count_list)):
            for k in range(1, max(orange_count_list[i:j+1])+1):
                orange_count = 0
                for l in range(i, j+1):
                    if orange_count_list[l] >= k:
                        orange_count += k
                if orange_count > max_orange_count:
                    max_orange_count = orange_count
    return max_orange_count

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            x = min(A[i:j+1])
            ans = max(ans, (j-i+1)*x)
    print(ans)

=======
Suggestion 8

def main():
    print('Hello World!')

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for l in range(n):
        x = a[l]
        for r in range(l, n):
            x = min(x, a[r])
            ans = max(ans, x * (r - l + 1))
    print(ans)
