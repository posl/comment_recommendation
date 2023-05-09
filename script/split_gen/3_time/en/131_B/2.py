def main():
    N, L = map(int, input().split())
    if L <= 0 and L+N-1 >= 0:
        print(sum([i for i in range(L, L+N)]))
    elif L <= 0 and L+N-1 < 0:
        print(sum([i for i in range(L, L+N)]) - L+N-1)
    elif L > 0:
        print(sum([i for i in range(L, L+N)]) - L)
