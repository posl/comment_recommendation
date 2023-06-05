def main():
    r,c = map(int,input().split())
    A = []
    for i in range(2):
        A.append(list(map(int,input().split())))
    print(A[r-1][c-1])

if __name__ == '__main__':
    main()