def main():
    N, M = map(int, input().split())
    foods = [0] * M
    for i in range(N):
        K, *A = map(int, input().split())
        for a in A:
            foods[a - 1] += 1
    print(sum([1 for f in foods if f == N]))
