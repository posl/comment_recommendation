def main():
    # A,B,C = map(int,input().split())
    A,B,C = 1,2,3
    A,B = B,A
    A,C = C,A
    print(A,B,C)

if __name__ == '__main__':
    main()