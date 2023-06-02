Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    a = a[0:n]
    a_set = set(a)
    max_even = -1
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0:
                max_even = max(max_even, a[i] + a[j])
    print(max_even)

=======
Suggestion 2

def solution(n, a):
    a.sort()
    if a[0] == 0:
        return -1
    elif a[-1] % 2 == 0:
        return a[-1]
    else:
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (a[i] + a[j]) % 2 == 0:
                    return a[i] + a[j]
        return -1

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = -1
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0:
                ans = max(ans, a[i] + a[j])
                break
    print(ans)

=======
Suggestion 4

def solve(n, a):
    a.sort()
    max_even = -1
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0:
                max_even = max(max_even, a[i] + a[j])
    return max_even

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_even = -1
    for i in range(N-1):
        for j in range(i+1,N):
            if (A[i]+A[j]) % 2 == 0:
                max_even = max(max_even, A[i]+A[j])
    print(max_even)

=======
Suggestion 6

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max_even = -1
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % 2 == 0:
                max_even = max(max_even, a[i] + a[j])
    print(max_even)

=======
Suggestion 7

def find_even_sum(n, a):
    a.sort()
    max_even = -1
    for i in range(n-1):
        for j in range(i+1, n):
            if (a[i]+a[j])%2==0:
                max_even = max(max_even, a[i]+a[j])
            elif a[i]+a[j]>max_even:
                break
    return max_even

=======
Suggestion 8

def findEvenSum(arr):
    evenList = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            evenList.append(i)
    if len(evenList) == 0:
        return -1
    else:
        evenSum = 0
        for i in range(len(evenList)):
            for j in range(i+1, len(evenList)):
                if arr[evenList[i]] + arr[evenList[j]] > evenSum:
                    evenSum = arr[evenList[i]] + arr[evenList[j]]
        return evenSum

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 检查是否有偶数
    for i in range(n):
        if a[i] % 2 == 0:
            print(a[i])
            return

    # 如果没有偶数，则检查是否有两个奇数之和为偶数
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % 2 == 0:
                print(a[i] + a[j])
                return

    print(-1)

=======
Suggestion 10

def findEvenSum(list):
    evenSum = -1
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if (list[i]+list[j])%2==0:
                if evenSum<list[i]+list[j]:
                    evenSum = list[i]+list[j]
    return evenSum
