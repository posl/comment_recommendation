def main():
    A,B,C = map(int,input().split())
    for i in range(A,B+1):
        if i%C == 0:
            print(i)
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()