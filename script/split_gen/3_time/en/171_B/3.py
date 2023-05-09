def main():
    N, K = map(int, input().split())
    price = list(map(int, input().split()))
    price.sort()
    print(sum(price[:K]))
