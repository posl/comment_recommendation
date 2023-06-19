def main():
    N, K = map(int, input().split())
    result = 0
    while N > 0:
        result += 1
        N = N // K
    print(result)

if __name__ == '__main__':
    main()