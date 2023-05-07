def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i == N-1 or A[i] != A[i+1]:
            ans += 1
    print(ans)
