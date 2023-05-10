def main():
    h, w = map(int, input().split())
    for i in range(h):
        print(input().count('#'))

if __name__ == '__main__':
    main()