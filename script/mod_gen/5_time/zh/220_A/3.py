def main():
    A,B,C = map(int,input().split())
    if A % C == 0:
        print(A)
    else:
        print(-1)

if __name__ == '__main__':
    main()