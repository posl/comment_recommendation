def main():
    n = int(input())
    login = [0] * (10**9 + 2)
    for _ in range(n):
        a, b = map(int, input().split())
        login[a] += 1
        login[a+b] -= 1
    for i in range(1, 10**9 + 2):
        login[i] += login[i-1]
    print(*login[1:-1])
