def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += (A[i+1]-A[i])*(i+1)*(N-i-1)
    print(ans)
