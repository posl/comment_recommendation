def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum([ai - 10 if ai > 10 else 0 for ai in a]))

if __name__ == '__main__':
    main()