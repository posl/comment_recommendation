def main():
    A, B = map(int, input().split())
    print(max(A+B, A+B-1, A+B-2))

if __name__ == '__main__':
    main()