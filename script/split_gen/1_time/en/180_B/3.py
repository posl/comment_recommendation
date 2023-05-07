def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum(map(abs, x)))
    print((sum(map(lambda i: i ** 2, x))) ** 0.5)
    print(max(map(abs, x)))
