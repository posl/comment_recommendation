def main():
    N, L = map(int, input().split())
    apple_pie = 0
    min_diff = 10000
    for i in range(1, N+1):
        apple = L + i - 1
        apple_pie = apple_pie + apple
        if min_diff > abs(apple):
            min_diff = abs(apple)
            min_apple = apple
    print(apple_pie - min_apple)

if __name__ == '__main__':
    main()