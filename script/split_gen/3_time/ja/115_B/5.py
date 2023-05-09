def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    max_p = max(p)
    p.remove(max_p)
    print(sum(p) + max_p // 2)
