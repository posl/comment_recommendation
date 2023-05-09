def main():
    import sys
    readline = sys.stdin.readline
    N, L = map(int, readline().split())
    apple = [L+i-1 for i in range(1, N+1)]
    if 0 in apple:
        print(sum(apple))
    else:
        if max(apple) > 0:
            print(sum(apple)-max(apple))
        else:
            print(sum(apple)-min(apple))
