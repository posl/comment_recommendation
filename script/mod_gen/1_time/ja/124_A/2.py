def main():
    A, B = map(int, input().split())
    print(max(A+B, A+A-1, B+B-1))
main()

if __name__ == '__main__':
    main()