def main():
    n, k = map(int, input().split())
    s = input()
    start = s[0]
    count = 0
    for i in range(1, n):
        if s[i] == start:
            count += 1
    print(min(count + 2 * k, n - 1))
