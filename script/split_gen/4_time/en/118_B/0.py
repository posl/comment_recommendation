def main():
    N, M = map(int, input().split())
    foods = set(range(1, M + 1))
    for _ in range(N):
        foods &= set(map(int, input().split()[1:]))
    print(len(foods))
