def main():
    n = int(input())
    p = [int(input()) for i in range(n)]
    print(sum(p) - max(p) + max(p) // 2)
