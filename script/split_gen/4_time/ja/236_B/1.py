def main():
    import sys
    readline = sys.stdin.readline
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    d = {}
    for a in A:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    for a in d:
        if d[a] % 2 == 1:
            print(a)
            exit()
