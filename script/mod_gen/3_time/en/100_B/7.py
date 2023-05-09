def main():
    D, N = (int(x) for x in input().split())
    if N == 100:
        N += 1
    print(N * 100 ** D)

if __name__ == '__main__':
    main()