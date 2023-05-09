def main():
    N, K = map(int, input().split())
    p = 0
    for n in range(1, N+1):
        p += (1/N) * (1/2)**(1 + (K-1)//n)
    print(p)
