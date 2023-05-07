def main():
    N, M = map(int, input().split())
    balls = [0] * (N + 1)
    for _ in range(M):
        _, *a = map(int, input().split())
        for i in a:
            balls[i] += 1
    print("Yes" if all(i % 2 == 0 for i in balls) else "No")
