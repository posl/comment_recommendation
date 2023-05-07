def main():
    N, M = map(int, input().split())
    foods = [set() for _ in range(N)]
    for i in range(N):
        K, *A = map(int, input().split())
        foods[i] = set(A)
    ans = 0
    for i in range(1, M+1):
        if all(i in food for food in foods):
            ans += 1
    print(ans)
