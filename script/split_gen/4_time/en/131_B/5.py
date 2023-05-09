def main():
    N, L = map(int, input().split())
    print(sum(list(range(L+1, L+N))) - min(range(L+1, L+N), key=lambda x:abs(x)))
