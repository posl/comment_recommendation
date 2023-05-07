def main():
    N, M = map(int, input().split())
    foods = set()
    for _ in range(N):
        foods = foods | set(map(int, input().split()[1:]))
    print(len(foods))
