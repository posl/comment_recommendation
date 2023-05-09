def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(n//2):
        if A[i] != A[n-1-i]:
            ans += 1
    print(ans)
