def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N**0.5)+1):
        while N % i == 0:
            N //= i
            ans += 1
    if N != 1:
        ans += 1
    print(ans)
