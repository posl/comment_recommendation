def main():
    A,B,C = list(map(int, input().split()))
    if A%C == 0:
        print(A)
    else:
        for i in range(A+1,B+1):
            if i%C == 0:
                print(i)
                break
        else:
            print(-1)

if __name__ == '__main__':
    main()