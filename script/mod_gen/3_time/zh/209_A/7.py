def main():
    A, B = map(int, input().split())
    print(B - A + 1 if B >= A else 0)

if __name__ == '__main__':
    main()