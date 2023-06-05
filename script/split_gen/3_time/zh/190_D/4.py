def solve(N):
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            if (N//i-i)%2 == 1:
                ans += 1
    return ans*2
N = int(input())
print(solve(N))
