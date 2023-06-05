def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, 2**N):
        sum = 0
        count = 0
        for j in range(N):
            if (i>>j)&1:
                sum += A[j]
                count += 1
        if sum % count == 0:
            ans += 1
    print(ans)
