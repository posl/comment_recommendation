def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i * (i + 1) // 2 > N:
            break
        if (N - i * (i + 1) // 2) % i == 0:
            ans += 1
    print(ans * 2)
