def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    result = 1
    for i in range(n):
        result = result * (c[i] - i) % (10**9 + 7)
    print(result)
