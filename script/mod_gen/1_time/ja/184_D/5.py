def main():
    A, B, C = map(int, input().split())
    print(100*(A*B+B*C+C*A)/(A+B+C)/(A*B+B*C+C*A))

if __name__ == '__main__':
    main()