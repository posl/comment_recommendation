def main():
    N = int(input())
    for i in range(N):
        print(*[binomial(i, j) for j in range(i + 1)])
