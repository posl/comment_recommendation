def main():
    N = int(input())
    print((10**N - 2*9**N + 8**N) % (10**9 + 7))

if __name__ == '__main__':
    main()