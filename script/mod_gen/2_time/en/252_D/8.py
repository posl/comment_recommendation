def  main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    A.sort()
    ans = 0
    for i in range(1, N+1):
        ans += (i-1) * (N-i) * (A[i+1] - A[i-1])
    print(ans)

if __name__ == '__main__':
    ()