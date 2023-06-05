def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += A[i]
    ans = 0
    for i in range(N):
        if (sum % A[i] == 0):
            ans += 1
    print(ans)
    
main()
