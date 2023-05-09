def main():
    N = int(input())
    AB = [map(int, input().split()) for _ in range(N)]
    A, B = [list(i) for i in zip(*AB)]
    print(min(A) + min(B))
