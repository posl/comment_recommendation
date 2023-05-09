def main():
    N = int(input())
    ans = 0
    for p in range(2, int(N**0.5)+1):
        while N%p == 0:
            N //= p
            ans += 1
    if N > 1:
        ans += 1
    print(ans)
