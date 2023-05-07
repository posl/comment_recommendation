def main():
    n = int(input())
    print(sum(1 for i in range(1, n + 1) if (i % 2) and (len([1 for j in range(1, i + 1) if i % j == 0]) == 8)))
