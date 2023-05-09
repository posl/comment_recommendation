def main():
    A,B,C = map(int, input().split())
    print(100*(A+B+C-1)/(A+B+C))

if __name__ == '__main__':
    main()