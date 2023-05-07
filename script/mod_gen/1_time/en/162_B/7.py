def main():
    N = int(input())
    print(sum([i for i in range(1, N+1) if i%3 != 0 and i%5 != 0]))

if __name__ == '__main__':
    main()