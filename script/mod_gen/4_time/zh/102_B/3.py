def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_num = max(a)
    min_num = min(a)
    print(max_num - min_num)

if __name__ == '__main__':
    main()