def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    ans = 0
    for i in range(1, N):
        if A[i] != A[i-1]:
            ans += 1
    print(ans+1)
