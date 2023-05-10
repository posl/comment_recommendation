def main():
    n = int(input())
    p = [int(input()) for i in range(n)]
    p.sort()
    print(int(sum(p[:-1]) + p[-1] / 2))
