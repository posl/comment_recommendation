def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    p[-1] = int(p[-1] / 2)
    print(sum(p))
