def main():
    n, a, b = map(int, input().strip().split())
    print(min(a*n, b))
