def main():
    A,B,C = map(int,input().split())
    print(C if A >= B+C else A+B)

if __name__ == '__main__':
    main()