def main():
    X, Y = map(int, input().split())
    print(max(0, -(-Y//10) - X//10))

if __name__ == '__main__':
    main()