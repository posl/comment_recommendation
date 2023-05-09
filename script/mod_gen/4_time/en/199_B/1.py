def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    print(max(min(b) - max(a) + 1, 0))

if __name__ == '__main__':
    main()