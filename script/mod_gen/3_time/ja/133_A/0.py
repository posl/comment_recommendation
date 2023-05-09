def main():
    N, A, B = map(int, input().split())
    train = N * A
    taxi = B
    if train < taxi:
        print(train)
    else:
        print(taxi)

if __name__ == '__main__':
    main()