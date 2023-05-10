def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            A.append(int(query[1]))
        elif query[0] == "2":
            x = int(query[1])
            k = int(query[2])
            count = 0
            for a in A:
                if a <= x:
                    count += 1
            if count < k:
                print(-1)
            else:
                B = []
                for a in A:
                    if a <= x:
                        B.append(a)
                B.sort(reverse=True)
                print(B[k-1])
        elif query[0] == "3":
            x = int(query[1])
            k = int(query[2])
            count = 0
            for a in A:
                if a >= x:
                    count += 1
            if count < k:
                print(-1)
            else:
                B = []
                for a in A:
                    if a >= x:
                        B.append(a)
                B.sort()
                print(B[k-1])

if __name__ == '__main__':
    main()