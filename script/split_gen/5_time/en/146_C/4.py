def main():
    a, b, x = map(int, input().split())
    print(max([n for n in range(1, 10**9) if a * n + b * len(str(n)) <= x]))
