def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(N * max(a) - sum(a))
