def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    print(T[N-1]+T[N-2])

if __name__ == '__main__':
    main()