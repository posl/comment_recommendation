def main():
    k, x = map(int, input().split())
    start = x - k + 1
    end = x + k
    for i in range(start, end):
        print(i, end=" ")

if __name__ == '__main__':
    main()