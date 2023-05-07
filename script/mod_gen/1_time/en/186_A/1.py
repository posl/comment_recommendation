def main():
    input = sys.stdin.readline
    N, W = map(int, input().split())
    print(N//W)

if __name__ == '__main__':
    main()