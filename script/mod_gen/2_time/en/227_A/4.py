def problem227_a():
    n, k, a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        print(k%n)

if __name__ == '__main__':
    problem227_a()