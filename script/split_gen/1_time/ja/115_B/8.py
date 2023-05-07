def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    print(sum(p[0:N-1]) + p[N-1]//2)
