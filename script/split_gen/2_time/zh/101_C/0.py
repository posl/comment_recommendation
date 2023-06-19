def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k == 2:
        print(n - 1)
        return
    result = 0
    for i in range(0, n, k - 1):
        result += 1
    print(result - 1)
