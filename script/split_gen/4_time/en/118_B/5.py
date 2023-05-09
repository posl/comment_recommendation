def main():
    N, M = map(int, input().split())
    foods = [0] * M
    for _ in range(N):
        a = list(map(int, input().split()))
        for i in range(1, a[0] + 1):
            foods[a[i] - 1] += 1
    print(foods.count(N))
