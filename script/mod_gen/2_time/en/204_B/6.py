def main():
    n = int(input())
    a = map(int, input().split())
    print(sum(max(0, x - 10) for x in a))

if __name__ == '__main__':
    main()