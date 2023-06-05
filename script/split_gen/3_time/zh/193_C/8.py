def main():
    N = int(input())
    ans = N
    for i in range(2, int(N ** 0.5) + 1):
        x = i * i
        while x <= N:
            ans -= 1
            x *= i
    print(ans)
