def main():
    N, L = map(int, input().split())
    apple_pie = [L + i - 1 for i in range(1, N + 1)]
    print(sum(apple_pie) - min(apple_pie, key=abs))
