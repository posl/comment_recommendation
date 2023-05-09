def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum(map(abs, x)))
    print(sum(map(lambda x: x ** 2, x)) ** 0.5)
    print(max(map(abs, x)))
