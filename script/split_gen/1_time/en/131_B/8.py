def main():
    N, L = map(int, input().split())
    print(N*(L-1)+N*(N+1)//2)
