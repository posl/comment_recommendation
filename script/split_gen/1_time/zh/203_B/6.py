def main():
    N, K = map(int, input().split())
    print(sum([int(str(i) + str(j)) for i in range(1, N + 1) for j in range(1, K + 1)]))
