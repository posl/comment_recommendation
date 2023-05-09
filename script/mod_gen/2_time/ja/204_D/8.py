def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    print(sum(T) - T[0] + T[0] // 2)

if __name__ == '__main__':
    main()