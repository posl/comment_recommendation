def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    q = int(input())
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            A[int(query[1])-1] = int(query[2])
        elif query[0] == '2':
            print(A[int(query[1])-1])

if __name__ == '__main__':
    main()