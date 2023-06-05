def main():
    A = []
    for i in range(2):
        A.append([int(i) for i in input().split()])
    print(A[0][0]*A[1][1]-A[0][1]*A[1][0])

if __name__ == '__main__':
    main()