def main():
    N, K = map(int, input().split())
    print(1 if N%K else 0)

if __name__ == '__main__':
    main()