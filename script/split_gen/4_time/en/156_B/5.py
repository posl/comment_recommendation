def main():
    n, k = map(int, input().split())
    if n == 0:
        print(0)
        return
    result = 0
    while n > 0:
        n //= k
        result += 1
    print(result)
