def main():
    N = int(input())
    path = [list(map(int, input().split())) for i in range(N-1)]
    print(path)
    print(N)

if __name__ == '__main__':
    main()