def main():
    A,B = map(int,input().split())
    print(max(A+B,A+B-1,A-1+B-1))

if __name__ == '__main__':
    main()