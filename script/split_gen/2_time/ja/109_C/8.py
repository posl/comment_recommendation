def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    print(max([max([x[i] - X, X - x[i]]) for i in range(N)]) // 2)
