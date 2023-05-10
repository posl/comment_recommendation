def main():
    n = int(input())
    ladders = [list(map(int, input().split())) for _ in range(n)]
    ladders = sorted(ladders, key=lambda x: x[1])
    print(ladders[-1][1] - 1)

if __name__ == '__main__':
    main()