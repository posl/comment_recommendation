def main():
    N, L = map(int, input().split())
    flavor = [L+i-1 for i in range(1, N+1)]
    print(sum(flavor)-min(flavor, key=abs))
