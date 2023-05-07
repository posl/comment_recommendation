def main():
    N = int(input())
    print(sum([i for i in range(1, N + 1) if i % 3 != 0 and i % 5 != 0]) + 2 * sum([i for i in range(1, N + 1) if i % 3 == 0 and i % 5 != 0]) + 4 * sum([i for i in range(1, N + 1) if i % 3 != 0 and i % 5 == 0]) + 15 * sum([i for i in range(1, N + 1) if i % 3 == 0 and i % 5 == 0]))
