def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] == ans:
            ans += 1
    print(ans)
