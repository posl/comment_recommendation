def main():
    n, a, b = map(int, input().split())
    taxi = n * b
    train = n * a
    if taxi <= train:
        print(taxi)
    else:
        print(train)

if __name__ == '__main__':
    main()