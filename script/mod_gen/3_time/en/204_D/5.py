def main():
    N = int(input())
    T = [int(_) for _ in input().split()]
    T.sort()
    print(sum(T) - T[-1] + T[-1] // 2)

if __name__ == '__main__':
    main()