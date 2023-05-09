def main():
    N = int(input())
    print(len([i for i in range(1, N + 1, 2) if len([j for j in range(1, i + 1) if i % j == 0]) == 8]))
