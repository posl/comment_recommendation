def main():
    # input
    A, B, C = map(int, input().split())
    # compute
    # output
    print(max(A+B+C, A+B*C, A*B+C, A*B*C))

if __name__ == '__main__':
    main()