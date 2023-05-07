def main():
    N, M = map(int, input().split())
    dishes = set()
    for _ in range(N):
        K, *A = map(int, input().split())
        dishes |= set(A)
    print(len(dishes))
