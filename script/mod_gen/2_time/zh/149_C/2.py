def main():
    A,B,K = map(int,input().split())
    if K <= A:
        print(A-K,B)
    elif K > A and K <= A+B:
        print(0,B-(K-A))
    else:
        print(0,0)

if __name__ == '__main__':
    main()