def main():
    N = int(input())
    login = [0] * (10**9 + 2)
    for i in range(N):
        A, B = map(int, input().split())
        login[A] += 1
        login[A + B] -= 1
    for i in range(10**9 + 1):
        login[i + 1] += login[i]
    for i in range(1, N + 1):
        ans = 0
        for j in range(10**9 + 1):
            if login[j] == i:
                ans += 1
        print(ans)
