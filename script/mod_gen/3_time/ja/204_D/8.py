def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    print(T[-1])

if __name__ == '__main__':
    main()