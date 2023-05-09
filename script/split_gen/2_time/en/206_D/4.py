def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N//2):
        if A[i] != A[-i-1]:
            ans += 1
    print(ans)
