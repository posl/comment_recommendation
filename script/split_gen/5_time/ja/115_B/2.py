def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort()
    print(sum(p) - int(p[-1] / 2))
