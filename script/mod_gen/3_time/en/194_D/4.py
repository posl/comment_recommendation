def main():
    N = int(input())
    print(sum([i * (1 / N) ** i for i in range(1, N + 1)]))

if __name__ == '__main__':
    main()