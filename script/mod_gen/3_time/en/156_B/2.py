def main():
    import math
    N, K = map(int, input().split())
    print(math.ceil(math.log(N, K)))

if __name__ == '__main__':
    main()