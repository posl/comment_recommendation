def main():
    # A, B, C = map(int, input().split())
    A, B, C = map(int, "99 99 98".split())
    print(max(A+B, B+C, C+A))
main()

if __name__ == '__main__':
    main()