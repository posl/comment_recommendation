def main():
    N = int(input())
    P = [int(input()) for i in range(N)]
    P.sort()
    P[-1] = P[-1] // 2
    print(sum(P))
