def main():
    a, b, x = map(int, input().split())
    max_n = 10**9
    min_n = 0
    while max_n - min_n > 1:
        n = (max_n + min_n) // 2
        if a * n + b * len(str(n)) > x:
            max_n = n
        else:
            min_n = n
    print(min_n)
