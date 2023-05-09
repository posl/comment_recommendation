def main():
    N, L = map(int, input().split())
    apple = [L + i - 1 for i in range(1, N + 1)]
    print(sum(apple) - min(apple, key=abs))
