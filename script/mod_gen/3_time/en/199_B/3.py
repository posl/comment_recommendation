def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(min(b) - max(a) + 1 if max(a) <= min(b) else 0)

if __name__ == '__main__':
    main()