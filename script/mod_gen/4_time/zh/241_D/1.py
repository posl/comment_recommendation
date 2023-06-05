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
            tmp = [a for a in A if a <= x]
            tmp.sort(reverse=True)
            if len(tmp) >= k:
                print(tmp[k-1])
            else:
                print(-1)
        else:
            x = int(query[1])
            k = int(query[2])
            tmp = [a for a in A if a >= x]
            tmp.sort()
            if len(tmp) >= k:
                print(tmp[k-1])
            else:
                print(-1)

if __name__ == '__main__':
    main()