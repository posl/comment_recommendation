def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(len(list(filter(lambda x: x % 2 == 1, map(int, input().split())))))

if __name__ == '__main__':
    main()