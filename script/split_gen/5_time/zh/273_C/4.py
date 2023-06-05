def main():
    input()
    A = list(map(int, input().split()))
    A.sort()
    n = len(A)
    ans = [0] * n
    for i in range(n):
        if i > 0 and A[i] == A[i - 1]:
            ans[i] = ans[i - 1]
            continue
        l = 0
        r = n
        while r - l > 1:
            m = (l + r) // 2
            if A[m] > A[i]:
                r = m
            else:
                l = m
        ans[i] = l
    for i in ans:
        print(i)
