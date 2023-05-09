def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(abs(max(a) - min(a)))

if __name__ == '__main__':
    main()