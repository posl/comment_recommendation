def main():
    A, B, C = map(int, input().split())
    print(max(A+B+C, A+B-C, A*B+C, A*B-C, A-B+C, A-B-C))

if __name__ == '__main__':
    main()