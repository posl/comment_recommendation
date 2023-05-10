def main():
    n, m = map(int, input().split())
    count = 0
    for i in range(1, m + 1):
        if m % i == 0:
            count += 1
    print(count)
