def main():
    k, x = map(int, input().split())
    print(*list(range(x-(k-1), x+k)))

if __name__ == '__main__':
    main()