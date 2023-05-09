def main():
    h, w = map(int, input().split())
    for i in range(h):
        a = list(map(int, input().split()))
        print(*a[::-1])

if __name__ == '__main__':
    main()