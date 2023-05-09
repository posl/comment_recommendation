def main():
    n, a, b = map(int, input().split())
    sum = 0
    for i in range(1, n + 1):
        if i % a == 0 or i % b == 0:
            continue
        sum += i
    print(sum)
