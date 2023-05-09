def main():
    N = int(input())
    ans = 0
    for i in range(2, N+1):
        if i*i > N:
            break
        while N % i == 0:
            N //= i
            ans += 1
    if N > 1:
        ans += 1
    print(ans)
