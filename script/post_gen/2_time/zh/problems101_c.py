Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    while True:
        if len(set(a)) == 1:
            break
        min_value = min(a)
        min_index = a.index(min_value)
        for i in range(min_index, min_index+k):
            a[i] = min_value
        count += 1
    print(count)

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    if K == 1:
        print(N-1)
        return
    print((N-2)//(K-1)+1)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-k):
        if a[i] < a[i+k]:
            ans += 1
    print(ans)

=======
Suggestion 4

def solve(n, k, a):
    # Write your code here.
    # 1. find the minimum number in the list
    # 2. find the index of the minimum number
    # 3. find the index of the minimum number - k + 1
    # 4. replace the minimum number with the minimum number - k + 1
    # 5. repeat 1-4 until all the numbers in the list are equal
    # 6. return the number of times of the replacement
    # 7. if the minimum number - k + 1 < 1, return -1
    # 8. if all the numbers in the list are equal, return 0
    # 9. if the minimum number is 1, return 0
    # 10. if the minimum number is 2, return 1
    # 11. if the minimum number is 3, return 2
    # 12. if the minimum number is 4, return 3
    # 13. if the minimum number is 5, return 4
    # 14. if the minimum number is 6, return 5
    # 15. if the minimum number is 7, return 6
    # 16. if the minimum number is 8, return 7
    # 17. if the minimum number is 9, return 8
    # 18. if the minimum number is 10, return 9
    # 19. if the minimum number is 11, return 10
    # 20. if the minimum number is 12, return 11
    # 21. if the minimum number is 13, return 12
    # 22. if the minimum number is 14, return 13
    # 23. if the minimum number is 15, return 14
    # 24. if the minimum number is 16, return 15
    # 25. if the minimum number is 17, return 16
    # 26. if the minimum number is 18, return 17
    # 27. if the minimum number is 19, return 18
    # 28. if the minimum number is 20, return 19
    # 29. if the minimum

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        if n <= k:
            break
        n -= k
        ans += 1
    print(ans + 1)

=======
Suggestion 6

def get_min(a,b):
    if a < b:
        return a
    else:
        return b

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    n = N - K
    print(1 + (n + K - 2) // (K - 1))

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    cnt = 0
    if (n-1) % (k-1) == 0:
        cnt = (n-1) // (k-1)
    else:
        cnt = (n-1) // (k-1) + 1
    print(cnt)

=======
Suggestion 9

def main():
    # 读入输入
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # A.sort()
    # print(A)
    # A = [1, 2, 3, 4]
    # N = 4
    # K = 3
    # print(A)
    # print(N, K)
    # print(A[0:K])
    # print(A[K-1:N])

    # 选择k个连续的元素，然后用所选元素中的最小值替换每个所选元素的值。
    # 选择k个连续的元素，然后用所选元素中的最小值替换每个所选元素的值。
    # 选择k个连续的元素，然后用所选元素中的最小值替换每个所选元素的值。
    # 选择k个连续的元素，然后用所选元素中的最小值替换每个所选元素的值。
    # 选择k个连续的元素，然后用所选元素中的最小值替换每个所选元素的值。
    # 选择k个连续的元素，然后用所选元素中的最小值替换每个所选元素的值。
    # 选择k个连续的元素，然后用所选元素中的最小值替换每个所选元素的值。
    # 选择k个连续的元素，然后用所选元素中的最小值替换每个所选元素的值。

    # 选择k个连续的元素，然后用所选元素中的最小值替换每个所选元素的值。

    # 选择k个连续的元素，然后用所选元素中的最小值替换每个所选元素的值。
    # 选择k个连续的元素，然后用所选元素中的最小值替换

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    if k == 1:
        print(n-1)
    else:
        print((n-2)//(k-1)+1)
