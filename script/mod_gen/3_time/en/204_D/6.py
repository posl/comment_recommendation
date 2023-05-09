def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    if N == 1:
        print(T[0])
    else:
        print(sum(T) - (T[0] / 2))

if __name__ == '__main__':
    main()