def main():
    A, B, C = map(int, input().split())
    print(max(A+B+C, A*10+B+C, A+B*10+C, A+B+C*10))

if __name__ == '__main__':
    main()