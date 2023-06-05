def main():
    A,B,C = map(int, input().split())
    print(max(A+B,A+C,B+C))

if __name__ == '__main__':
    main()