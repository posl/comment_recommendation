def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort(reverse=True)
    print(int(p[0]/2 + sum(p[1:])))
