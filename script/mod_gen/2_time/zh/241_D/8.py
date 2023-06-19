def main():
    n = int(input())
    A = []
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            B = []
            for a in A:
                if a <= x:
                    B.append(a)
            B.sort(reverse=True)
            if len(B) < k:
                print(-1)
            else:
                print(B[k-1])
        elif query[0] == '3':
            x = int(query[1])
            k = int(query[2])
            B = []
            for a in A:
                if a >= x:
                    B.append(a)
            B.sort()
            if len(B) < k:
                print(-1)
            else:
                print(B[k-1])

if __name__ == '__main__':
    main()