def main():
    a, b = map(int, input().split())
    n = b - a - 1
    x = n * (n + 1) // 2
    print(x - a)
main()
