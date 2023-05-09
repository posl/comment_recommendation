def main():
    A,B = map(int,input().split())
    if A>B:
        A,B = B,A
    for i in range(B,1000000000):
        if A*i%B==0:
            print(A*i)
            break

if __name__ == '__main__':
    main()