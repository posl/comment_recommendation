def main():
    N = int(input())
    if N < 250:
        print(0)
        return
    ans = 0
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            j = N // i
            if i % 2 == 0 and i // 2 < j:
                ans += 1
            if j % 2 == 0 and j // 2 < i:
                ans += 1
    print(ans)
