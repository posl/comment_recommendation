def main():
    a, b = map(int, input().split())
    print(str(min(a, b)) * max(a, b))

if __name__ == '__main__':
    main()