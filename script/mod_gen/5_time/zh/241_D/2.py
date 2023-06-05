def main():
    n = int(input())
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            B = [y for y in A if y <= x]
            B.sort(reverse=True)
            if len(B) < k:
                print(-1)
            else:
                print(B[k-1])
        elif query[0] == '3':
            x = int(query[1])
            k = int(query[2])
            B = [y for y in A if y >= x]
            B.sort()
            if len(B) < k:
                print(-1)
            else:
                print(B[k-1])
        else:
            print('error')

if __name__ == '__main__':
    main()