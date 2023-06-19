def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    #process
    ans = 0
    for i in range(N):
        ans += A[i]
    #output
    print(ans)
