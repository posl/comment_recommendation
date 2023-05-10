def main():
    N = int(input())
    A = []
    for i in range(N):
        query = input().split()
        if query[0] == "1":
            A.append(int(query[1]))
        elif query[0] == "2":
            x = int(query[1])
            k = int(query[2])
            tmp = [a for a in A if a <= x]
            if len(tmp) < k:
                print(-1)
            else:
                print(sorted(tmp)[-k])
        else:
            x = int(query[1])
            k = int(query[2])
            tmp = [a for a in A if a >= x]
            if len(tmp) < k:
                print(-1)
            else:
                print(sorted(tmp)[k-1])
main()

if __name__ == '__main__':
    main()