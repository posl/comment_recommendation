def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    print(sum(h_i >= k for h_i in h))
