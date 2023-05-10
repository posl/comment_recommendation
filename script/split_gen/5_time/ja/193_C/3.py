def main():
    N = int(input())
    if N == 1:
        print(1)
        return
    ans = 0
    for i in range(2, int(N ** 0.5) + 1):
        tmp = i * i
        while tmp <= N:
            ans += 1
            tmp *= i
    print(N - ans)
