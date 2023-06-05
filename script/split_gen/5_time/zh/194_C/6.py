def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = 0
    for i in range(1,N):
        ans += (A[i]-A[i-1])**2
    print(ans)
