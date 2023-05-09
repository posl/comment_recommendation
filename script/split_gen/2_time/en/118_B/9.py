def main():
    N, M = map(int, input().split())
    foods = []
    for _ in range(N):
        K, *A = list(map(int, input().split()))
        foods.append(set(A))
    ans = 0
    for i in range(1, M+1):
        if all(i in food for food in foods):
            ans += 1
    print(ans)
