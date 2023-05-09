def main():
    N = int(input())
    T = [int(x) for x in input().split()]
    print(sum(T) - max(T) // 2)

if __name__ == '__main__':
    main()