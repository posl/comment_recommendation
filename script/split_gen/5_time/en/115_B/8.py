def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    max_p = max(p)
    total = sum(p)
    print((total - max_p) + (max_p // 2))
