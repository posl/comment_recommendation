def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1001):
        if all([A[j] <= i and i <= B[j] for j in range(N)]):
            ans += 1
    print(ans)
