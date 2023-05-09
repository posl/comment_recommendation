def main():
    n, a, b = map(int, input().split())
    total = 0
    for i in range(1, n + 1):
        if i % a != 0 and i % b != 0:
            total += i
    print(total)
