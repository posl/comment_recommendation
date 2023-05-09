def main():
    n, l = map(int, input().split())
    apple = [l+i for i in range(n)]
    sum_apple = sum(apple)
    min_apple = min(apple, key=abs)
    print(sum_apple - min_apple)
main()

if __name__ == '__main__':
    main()