def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sum = sum(A)
    A_max = max(A)
    index = A.index(A_max)
    ans = A_sum - A_max
    if index == 0:
        ans += A_max
    else:
        ans += min(A[index - 1], A[index + 1])
    print(ans)
