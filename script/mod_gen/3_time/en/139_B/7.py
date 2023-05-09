def main():
    A, B = map(int, input().split())
    print(B // A + (1 if B % A != 0 else 0))
main()

if __name__ == '__main__':
    main()