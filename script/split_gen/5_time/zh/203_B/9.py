def main():
    n, k = map(int, input().split())
    result = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            result += 100 * i + j
    print(result)
