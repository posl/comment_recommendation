def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a) * (n - 1) - sum(a))
