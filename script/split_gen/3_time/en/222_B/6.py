def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum(1 for i in a if i < p))
