def main():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    if (A * B) % 2 == 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()