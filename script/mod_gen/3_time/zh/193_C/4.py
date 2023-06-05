def main():
    n = int(input())
    a = []
    for i in range(2, 1001):
        x = i * i
        while x <= n:
            a.append(x)
            x *= i
    print(n - len(set(a)))

if __name__ == '__main__':
    main()