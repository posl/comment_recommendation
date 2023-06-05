def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(1 / sum(map(lambda x: 1 / x, A)))
