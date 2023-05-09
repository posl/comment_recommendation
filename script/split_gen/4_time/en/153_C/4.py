def main():
    n,k = map(int, input().split())
    h = sorted(map(int, input().split()), reverse=True)
    if k >= n:
        print(0)
    else:
        print(sum(h[k:]))
