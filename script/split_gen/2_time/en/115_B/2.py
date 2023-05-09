def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort()
    ans = sum(p[:-1]) + p[-1] // 2
    print(ans)
