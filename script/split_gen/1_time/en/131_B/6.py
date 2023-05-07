def main():
    N, L = map(int, input().split())
    print(sum([L + i for i in range(N)]) - max([L + i for i in range(N)]))
